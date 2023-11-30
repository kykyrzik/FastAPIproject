from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(SessionMiddleware, secret_key="some-random-string")  # need rework secret key