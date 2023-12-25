from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from src.config.setting import load_settings


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(SessionMiddleware, secret_key=load_settings().SECRET_KEY)