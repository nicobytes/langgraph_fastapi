dev:
    uv run langgraph dev

api-dev:
    uv run fastapi dev app.api.main:app

api-run:
    uv run fastapi run app.api.main:app
