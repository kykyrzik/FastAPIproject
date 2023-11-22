from typing import Optional, List

from src.services.database.models.book.book import Book
from src.services.database.repositories.base import CRUDBase
from src.common.schemas.book.book import BookDTO, UpdateBookDTO


class BookRepo(CRUDBase):
    model = Book

    async def add_book(self, data: BookDTO) -> Optional[BookDTO]:
        return await self._create(data.__dict__)

    async def get_book(self, book_id: str) -> Optional[BookDTO]:
        return await self._get(field=self.model, value=book_id)

    async def get_list_book(self, limit: int = 100) -> Optional[List[BookDTO]]:
        return await self._get_list(limit)

    async def update_book(self, book_id: str, data: UpdateBookDTO) -> Optional[BookDTO]:
        return await self._update(field=self.model, value=book_id, data=data.__dict__)

    async def delete_book(self, book_id: str) -> bool:
        return await self._delete(field=self.model, model_id=book_id)