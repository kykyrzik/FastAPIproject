from typing import Optional, List

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.book.genre import Genre
from src.common.schemas.book.genre import GenreInDB, GenreDTO
from src.common.converts.genre import convert_genre_model_to_dto


class GenreRepo(CRUDBase):
    model = Genre

    async def get_genre(self, genre_id: int) -> Optional[GenreInDB]:
        result = await self._get(field=self.model.id, value=genre_id)
        return convert_genre_model_to_dto(result)

    async def get_list_genre(self,
                             limit: int = 20,
                             offset: int = 0
                             ) -> Optional[List[GenreInDB]]:
        result = await self._get_list(limit, offset)
        total = [convert_genre_model_to_dto(i) for i in result]
        return total

    async def add_genre(self, data: GenreDTO) -> Optional[GenreInDB]:
        result = await self._create(data.__dict__)
        return convert_genre_model_to_dto(result)

    async def update_genre(self, data: GenreDTO, genre_id: int) -> GenreInDB:
        result = await self._update(field=self.model.id, value=genre_id, data=data.__dict__)
        return convert_genre_model_to_dto(result)
