from typing import Any

from fastapi import APIRouter, Depends

from src.common.schemas.book.author import AuthorsDTO
from src.services.database.repositories.book.author_repo import AuthorRepositories

router = APIRouter()


@router.post("/add_author")
async def add_author(data: AuthorsDTO,
                     crud: AuthorRepositories = Depends()
                     ) -> Any:
    result = await crud.create_author(data)
    return {"result": result,
            "message": "success"}


@router.get("/get_author/{author_id}")
async def get_author(author_id: int,
                     crud: AuthorRepositories = Depends()
                     ) -> Any:
    return await crud.get_author(author_id)


@router.get("/get_list_author")
async def get_list_author(limit: int = 20,
                          offset: int = 0,
                          crud: AuthorRepositories = Depends()
                          ) -> Any:
    return await crud.get_list_authors(limit, offset)


@router.patch(  "/update_author/{author_id}")
async def update_author(author_id: int,
                        data: AuthorsDTO,
                        crud: AuthorRepositories = Depends()
                        ) -> Any:
    return await crud.update_author(data, author_id)
