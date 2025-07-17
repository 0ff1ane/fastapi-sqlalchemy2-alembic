from fastapi import APIRouter
from inertia import (
    InertiaResponse,
)
from core.inertia import InertiaDependency

# views served on base path
views_router = APIRouter()

@views_router.get("/", response_model=None)
async def index(inertia: InertiaDependency) -> InertiaResponse:
     return await inertia.render('Index', {
          'name': 'John Doe'
     })
