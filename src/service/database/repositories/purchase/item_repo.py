from typing import List, Optional

from src.service.database.repositories.base import CRUDBase
from src.service.database.models.purchase.item import Item
from src.service.database.schemas.purchase.item import ItemDTO, BaseItem


class ItemRepo(CRUDBase):
    model = Item

    async def add_item(self, data: BaseItem) -> Optional[ItemDTO]:
        return await self._create(data=data.__dict__)

    async def get_item(self, item_id: int) -> Optional[ItemDTO]:
        return await self._get(field=self.model, value=item_id)

    async def get_list_item(self, limit: int = 10) -> Optional[List[ItemDTO]]:
        return await self._get_list(limit)
