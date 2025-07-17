from datetime import datetime
from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    content: str


class CreateTodoResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    updated_at: datetime


class RetrieveTodoResponse(BaseModel):
    id: int
    content: str
    is_completed: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime


class ListTodosResponseItem(BaseModel):
    id: int
    content: str
    is_completed: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime


class ListTodosResponse(BaseModel):
    count: int
    items: list[ListTodosResponseItem]


class UpdateTodoRequest(BaseModel):
    is_completed: bool
    is_deleted: bool


class UpdateTodoResponse(BaseModel):
    id: int
    content: str
    is_completed: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime
