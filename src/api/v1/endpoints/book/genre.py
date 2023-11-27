from typing import Any

from fastapi import APIRouter, Depends

from src.common.schemas.book.genre import GenreDTO
from src.services.database.repositories.book.genre_repo import GenreRepo

router = APIRouter()


@router.post("/add_genre")
async def add_author(data: GenreDTO,
                     crud: GenreRepo = Depends()
                     ) -> Any:
    result = await crud.add_genre(data)
    return {"result": result,
            "message": "success"}


@router.get("/get_genre/{genre_id}")
async def get_author(genre_id: int,
                     crud: GenreRepo = Depends()
                     ) -> Any:
    return await crud.get_genre(genre_id)


@router.get("/get_list_genre")
async def get_list_author(limit: int = 20,
                          offset: int = 0,
                          crud: GenreRepo = Depends()
                          ) -> Any:
    return await crud.get_list_genre(limit, offset)


@router.patch("/update_genre/{genre_id}")
async def update_genre(author_id: int,
                       data: GenreDTO,
                       crud: GenreRepo = Depends(),
                       ) -> Any:
    return await crud.update_genre(data, author_id)

