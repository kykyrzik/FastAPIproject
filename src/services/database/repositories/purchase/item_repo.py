from typing import Optional

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.purchase.item import Item
from src.common.schemas.purchase.item import ItemDTO


class ItemRepo(CRUDBase):
    model = Item

    async def add_item(self,
                       book_id: str,
                       amount_item: int
                       ) -> Optional[ItemDTO]:
        item = dict(book_id=book_id, amount_item=amount_item)
        return await self._create(item)
