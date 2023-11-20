from typing import Optional, List

from src.service.database.repositories.base import CRUDBase
from src.service.database.models.book.cover_type import CoverType
from src.common.schemas.book.cover_type import CoverTypeDTO


class CoverTypeRepo(CRUDBase):
    model = CoverType

    async def get_cover_type(self, cover_type_id: int) -> Optional[CoverTypeDTO]:
        return await self._get(field=self.model, value=cover_type_id)

    async def get_list_cover_type(self, limit: int = 3) -> Optional[List[CoverTypeDTO]]:
        return await self._get_list(limit)

    async def add_cover_type(self, data: CoverTypeDTO) -> Optional[CoverTypeDTO]:
        return await self._create(data=data.__dict__)

    async def delete_cover_type(self, cover_type_id: int) -> bool:
        return await self._delete(field=self.model, model_id=cover_type_id)
