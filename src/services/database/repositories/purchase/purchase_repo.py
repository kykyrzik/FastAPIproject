from typing import List, Optional

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.purchase.purchase import Purchase
from src.common.schemas.purchase.purchase import (PurchaseCreateDTO,
                                                  PurchaseInDB,
                                                  UpdateAddressDTO)
from src.common.converts.purchase import convert_purchase_model_to_dto


class PurchaseRepo(CRUDBase):
    model = Purchase

    async def add_purchase(self, data: PurchaseCreateDTO) -> Optional[PurchaseInDB]:
        return convert_purchase_model_to_dto(await self._create(data=data.__dict__))

    async def get_purchase(self, purchase_id: int) -> Optional[PurchaseInDB]:
        return convert_purchase_model_to_dto(await self._get(field=self.model.id, value=purchase_id))

    async def get_list_purchase(self, limit: int = 10,
                                offset: int = 0
                                ) -> Optional[List[PurchaseInDB]]:
        result = await self._get_list(limit, offset)
        return [convert_purchase_model_to_dto(item) for item in result]

    async def update_address(self, purchase_id: int, data: UpdateAddressDTO) -> Optional[PurchaseInDB]:
        return convert_purchase_model_to_dto(await self._update(field=self.model,
                                                                value=purchase_id,
                                                                data=data.__dict__)
                                             )
