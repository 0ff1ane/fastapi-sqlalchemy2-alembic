import os
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from inertia import InertiaVersionConflictException
from inertia import inertia_version_conflict_exception_handler

from core.inertia import inertia_config
from apps.todos.apis import router as todos_router
from views import views_router

api_router = APIRouter(prefix="/api")
api_router.include_router(todos_router, prefix="/todos")

app = FastAPI()

app.add_exception_handler(
    InertiaVersionConflictException,
    inertia_version_conflict_exception_handler
)

inertia_env = inertia_config.environment
cwd = os.path.dirname(__file__)
frontend_dir = (
    os.path.join(cwd, "..", "frontend", "dist")
    if inertia_config != "development"
    else os.path.join(cwd, "..", "frontend", "src")
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount(
    "/assets", StaticFiles(directory=os.path.join(frontend_dir, "assets")), name="assets"
)

app.include_router(api_router)
app.include_router(views_router)
