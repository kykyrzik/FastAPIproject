from fastapi import FastAPI, Depends
import uvicorn
from src.api.v1 import api


app = FastAPI()

app.include_router(api.router)


def main() -> None:
    uvicorn.run("main:app", host='127.0.0.1', port=8000)


if __name__ == "__main__":
    main()
