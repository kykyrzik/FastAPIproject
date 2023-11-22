from typing import List, Optional

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.book.author import Author
from src.common.schemas.book.author import AuthorsDTO


class AuthorRepositories(CRUDBase):
    model = Author

    async def get_author(self, author_id: int) -> Optional[str]:
        return await self._get(field=self.model, value=author_id)

    async def get_list_authors(self, limit: int = 20) -> Optional[List[str]]:
        return await self._get_list(limit)

    async def create_author(self, data: AuthorsDTO) -> AuthorsDTO:
        data = data.__dict__
        return await self._create(data)

    async def update_author(self, data: AuthorsDTO, author_id: Optional[int] = None) -> AuthorsDTO:
        id_author = data.__dict__.pop("id")
        data = data.__dict__
        if not author_id:
            return await self._update(field=self.model,
                                      value=id_author,
                                      data=data)
        return await self._update(field=self.model, value=author_id, data=data)
