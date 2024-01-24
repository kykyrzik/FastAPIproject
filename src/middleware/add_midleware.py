from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from src.config.setting import load_auth_jwt


def setup_middleware(web: FastAPI) -> None:
    web.add_middleware(SessionMiddleware, secret_key=load_auth_jwt().private_key_path)
