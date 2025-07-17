## FastAPI with SQLAlchemy2, Alemic, Pydantic, asyncpg. Frontend by Svelte 5 with InertiaJS
  Simple Todo App


## Reasons
Most of the FastAPI tutorials out there use SqlAlchemy 1.
Setting it up with SqlAlchemy 2 was a bit of a chore. Hope this helps someone out there.
A self-contained backend+frontend monorepo helps with e2e testing, typegen and deployment.


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
  * Add typegen from PyDantic to use in Typescript
  * Add SSR for backend
  * Add DockerFile
