from fastapi import Depends
from typing import Annotated
from inertia import (
    Inertia,
    InertiaConfig,
    inertia_dependency_factory,
)
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

# Your desired configuration
inertia_config = InertiaConfig(
    root_template_filename="base.html",
    entrypoint_filename="main.js",
    templates=templates
)

inertia_dependency = inertia_dependency_factory(
    inertia_config
)

InertiaDependency = Annotated[Inertia, Depends(inertia_dependency)]
