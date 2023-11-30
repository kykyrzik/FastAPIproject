from typing import Optional, List

from src.services.database.models.book.book import Book
from src.services.database.repositories.base import CRUDBase
from src.common.schemas.book.book import BookDTO, UpdateBookDTO
from src.common.converts.book import convert_book_model_to_dto


class BookRepo(CRUDBase):
    model = Book

    async def add_book(self, data: BookDTO) -> Optional[BookDTO]:
        return await self._create(data.__dict__)

    async def get_book(self, book_id: str) -> Optional[BookDTO]:
        return convert_book_model_to_dto(await self._get(field=self.model.ISBN, value=book_id))

    async def get_list_book(self, limit: int = 20, offset: int = 0) -> Optional[List[BookDTO]]:
        result = await self._get_list(limit, offset)
        return [convert_book_model_to_dto(item) for item in result]

    async def update_book(self, book_id: str, data: UpdateBookDTO) -> Optional[BookDTO]:
        return convert_book_model_to_dto(await self._update(field=self.model.id,
                                                            value=book_id,
                                                            data=data.__dict__)
                                         )

    async def delete_book(self, book_id: str) -> bool:
        return await self._delete(field=self.model.id, model_id=book_id)
