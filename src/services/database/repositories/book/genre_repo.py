from typing import Optional, List

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.book.genre import Genre
from src.common.schemas import GenreDTO


class GenreRepo(CRUDBase):
    model = Genre

    async def get_genre(self, genre_id: int) -> Optional[GenreDTO]:
        return await self._get(field=self.model, value=genre_id)

    async def get_list_genre(self, limit: int = 50) -> Optional[List[GenreDTO]]:
        return await self._get_list(limit)

    async def add_genre(self, data: GenreDTO) -> Optional[GenreDTO]:
        return await self._create(data.__dict__)

    async def update_genre(self, data: GenreDTO, genre_id: Optional[int] = None) -> GenreDTO:
        id_genre = data.__dict__.pop("id")
        data = data.__dict__
        if not genre_id:
            return await self._update(field=self.model,
                                      value=id_genre,
                                      data=data)
        return await self._update(field=self.model, value=genre_id, data=data)
