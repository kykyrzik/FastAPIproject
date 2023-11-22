from typing import Optional, List

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.book.rars import RARS
from src.common.schemas.book.rars import RARDDTO


class RARSRepo(CRUDBase):
    model = RARS

    async def get_rars(self, rars_id: int) -> Optional[RARDDTO]:
        return await self._get(field=self.model, value=rars_id)

    async def get_all_rars(self) -> Optional[List[RARDDTO]]:
        return await self._get_list(5)
