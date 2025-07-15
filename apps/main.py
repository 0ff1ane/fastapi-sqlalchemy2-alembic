from fastapi import APIRouter, FastAPI

from apps.todos.apis import router as todos_router

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(todos_router, prefix="/todos")

app = FastAPI()
app.include_router(v1_router)
