from typing import Annotated

from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_db_session
from apps.todos import models
from apps.todos import schemas

# /api/todo
router = APIRouter()

@router.post("", summary="Create a new todo")
async def create_todo(
    db: Annotated[AsyncSession, Depends(get_async_db_session)],
    request_data: schemas.CreateTodoRequest,
) -> schemas.CreateTodoResponse:
    todo = models.Todo(content=request_data.content)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return schemas.CreateTodoResponse(
        id=todo.id,
        content=todo.content,
        created_at=todo.created_at,
        updated_at=todo.updated_at,
    )


@router.get("/{todo_id}", summary="Retrieve a todo")
async def retrieve_todo(
    db: Annotated[AsyncSession, Depends(get_async_db_session)],
    todo_id: int,
) -> schemas.RetrieveTodoResponse:
    stmt = select(
        models.Todo.id,
        models.Todo.content,
        models.Todo.is_completed,
        models.Todo.is_deleted,
        models.Todo.created_at,
        models.Todo.updated_at,
    ).where(
        models.Todo.id == todo_id,
        models.Todo.is_deleted == False
    )
    result_row = (await db.execute(stmt)).first()

    if result_row is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    mapped_row = result_row._mapping
    return schemas.RetrieveTodoResponse(
        id=mapped_row[models.Todo.id],
        content=mapped_row[models.Todo.content],
        is_completed=mapped_row[models.Todo.is_completed],
        is_deleted=mapped_row[models.Todo.is_deleted],
        created_at=mapped_row[models.Todo.created_at],
        updated_at=mapped_row[models.Todo.updated_at],
    )


@router.get("", summary="List all todos")
async def list_todos(
    db: Annotated[AsyncSession, Depends(get_async_db_session)],
) -> schemas.ListTodosResponse:
    count_stmt = select(func.count(models.Todo.id)).where(
        models.Todo.is_deleted == False
    )
    count_result = (await db.execute(count_stmt)).scalar() or 0

    stmt = (
        select(
            models.Todo.id,
            models.Todo.content,
            models.Todo.is_completed,
            models.Todo.is_deleted,
            models.Todo.created_at,
            models.Todo.updated_at,
        )
        .where(
            models.Todo.is_deleted == False
        )
        .order_by(models.Todo.created_at.desc())
    )
    result_rows = (await db.execute(stmt)).all()

    return schemas.ListTodosResponse(
        count=count_result,
        items=[
            schemas.ListTodosResponseItem(
                id=row.id,
                content=row.content,
                is_completed=row.is_completed,
                is_deleted=row.is_deleted,
                created_at=row.created_at,
                updated_at=row.updated_at,
            )
            for row in result_rows
        ],
    )


@router.put("/{todo_id}", summary="Update a todo")
async def update_todo(
    db: Annotated[AsyncSession, Depends(get_async_db_session)],
    todo_id: int,
    request_data: schemas.UpdateTodoRequest,
) -> schemas.UpdateTodoResponse:
    stmt = select(models.Todo).where(
        models.Todo.id == todo_id,
        models.Todo.is_deleted == False
    )
    todo = (await db.execute(stmt)).scalar()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.is_completed = request_data.is_completed
    todo.is_deleted = request_data.is_deleted
    await db.commit()
    await db.refresh(todo)
    return schemas.UpdateTodoResponse(
        id=todo.id,
        content=todo.content,
        is_completed=todo.is_completed,
        is_deleted=todo.is_deleted,
        created_at=todo.created_at,
        updated_at=todo.updated_at,
    )


@router.delete("/{todo_id}", summary="Delete a todo", status_code=204)
async def delete_todo(
    db: Annotated[AsyncSession, Depends(get_async_db_session)],
    todo_id: int,
) -> None:
    stmt = select(models.Todo).where(
        models.Todo.id == todo_id,
        models.Todo.is_deleted == False
    )
    todo = (await db.execute(stmt)).scalar()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.is_deleted = True
    await db.commit()
    await db.refresh(todo)
    return None
