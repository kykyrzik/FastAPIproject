from typing import List, Optional

from src.service.database.repositories.base import CRUDBase
from src.service.database.models.purchase.purchase import Purchase
from src.common.schemas.purchase.purchase import (PurchaseInDB,
                                                  UpdateAddressDTO)


class PurchaseRepo(CRUDBase):
    model = Purchase

    async def add_purchase(self, data: PurchaseInDB) -> Optional[PurchaseInDB]:
        return await self._create(data=data.__dict__)

    async def get_purchase(self, purchase_id: int) -> Optional[PurchaseInDB]:
        return await self._get(field=self.model, value=purchase_id)

    async def get_list_purchase(self, limit: int = 10) -> Optional[List[PurchaseInDB]]:
        return await self._get_list(limit)

    async def update_address(self, purchase_id: int, data: UpdateAddressDTO) -> Optional[PurchaseInDB]:
        return await self._update(field=self.model, value=purchase_id, data=data.__dict__)
