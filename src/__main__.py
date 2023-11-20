from fastapi import FastAPI
import uvicorn

from src.api.v1 import api

app = FastAPI()

app.include_router(api.router, )


def main() -> None:
    uvicorn.run("main:app")


if __name__ == "__main__":
    main()
