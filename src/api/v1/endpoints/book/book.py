from fastapi import APIRouter, Depends, HTTPException

from src.common.schemas.book.book import BookDTO, UpdateBookDTO, ValidationISBN
from src.services.database.repositories.book.book_repo import BookRepo

router = APIRouter()


@router.post("/add_book")
async def add_book(book: BookDTO,
                   crud: BookRepo = Depends()
                   ) -> BookDTO:
    result = await crud.add_book(book)
    return {"result": result,
            "message": "confirm"}


@router.get("/get_book/{book_id}")
async def get_book(book_id: str,
                   crud: BookRepo = Depends()
                   ) -> BookDTO:
    return await crud.get_book(book_id)


@router.get("/get_list")
async def get_list_book(limit: int = 100,
                        crud: BookRepo = Depends()
                        ) -> list[BookDTO]:
    return await crud.get_list_book(limit)


@router.patch("/update_data_about_the_book/{book_id}")
async def update_book(data: UpdateBookDTO,
                      book_id: str,
                      crud: BookRepo = Depends()
                      ) -> UpdateBookDTO:
    if ValidationISBN(ISBN=book_id) is None:
        raise HTTPException(status_code=404, detail="book does not exists")
    return await crud.update_book(book_id, data)


@router.delete("/delete_book/{book_id}")
async def delete_book(book_id: str,
                      crud: BookRepo = Depends()
                      ) -> bool:
    if ValidationISBN(ISBN=book_id) is None:
        raise HTTPException(status_code=404, detail="book does not exists")
    result = await crud.delete_book(book_id)
    if result:
        return {'message': "success"}
