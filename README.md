## FastAPI with SQLAlchemy2, Alemic, Pydantic, asyncpg. Frontend by Svelte 5 with InertiaJS
  Simple Todo App


## Setup
  * Clone this repo
  * Backend setup
    * Dependencies are in pyproject.toml. Install using `poetry` or `uv`
    * Edit the .env file with your DB credentials
    * Run `uv run alembic upgrade head` to run migrations
    * Run the server with `poetry run python server.py` or `uv run python server.py` depending on what you use
    * Visit http://localhost:8000/docs for the OpenAPI playground
  * Frontend setup
    * Go to `./frontend` directory
    * Run `npm install`
    * Run `npm run dev`
  * Visit http://localhost:8000 to see a simple Todo app tied to the backend and DB


## References
  * FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
  * SqlAlchemy 2: [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
  * Pydantic: [https://docs.pydantic.dev/](https://docs.pydantic.dev/)
  * FastAPI-Inertia: [https://github.com/hxjo/fastapi-inertia/](https://github.com/hxjo/fastapi-inertia/)
  * InertiaJS: [inertiajs.com](inertiajs.com)


## TODO
  * Add backend tests
  * Add frontend tests
  * Add SSR for backend
  * Add DockerFile
