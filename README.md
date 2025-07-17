## FastAPI with SQLAlchemy2, Alemic, Pydantic, asyncpg
  Simple Todo App backend


# For a setup with InertiaJS serving Svelte file. Check this [branch](https://github.com/0ff1ane/fastapi-sqlalchemy2-alembic/tree/inertia-svelte)


## Setup
  * Clone this repo
  * Dependencies are in pyproject.toml. Install using `poetry` or `uv`
  * Edit the .env file with your DB credentials
  * Run `uv run alembic upgrade head` to run migrations
  * Run the server with `poetry run python server.py` or `uv run python server.py` depending on what you use
  * Visit http://localhost:8000/docs for the OpenAPI playground


## References
  * FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
  * SqlAlchemy 2: [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)


## TODO
  * Add backend tests
  * Add DockerFile
