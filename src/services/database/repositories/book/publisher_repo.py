from typing import Optional, List

from src.services.database.models.book.publisher import Publisher
from src.common.schemas.book.publisher import PublisherDTO
from src.services.database.repositories.base import CRUDBase


class PublisherRepo(CRUDBase):
    model = Publisher

    async def get_publisher(self, publisher_id: int) -> Optional[PublisherDTO]:
        return await self._get(field=self.model, value=publisher_id)

    async def get_list_publisher(self, limit: int = 20) -> Optional[List[PublisherDTO]]:
        return await self._get_list(limit)

    async def add_publisher(self, data: PublisherDTO) -> Optional[PublisherDTO]:
        return await self._create(data=data.__dict__)

    async def delete_publisher(self, publisher_id: int) -> bool:
        return await self._delete(field=self.model, model_id=publisher_id)

    async def update_publisher(self, data: PublisherDTO, publisher_id: Optional[int] = None) -> Optional[PublisherDTO]:
        id_publisher = data.__dict__.pop("id")
        data = data.__dict__
        if not publisher_id:
            return await self._update(field=self.model,
                                      value=id_publisher,
                                      data=data)
        return await self._update(field=self.model, value=publisher_id, data=data)