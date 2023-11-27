from typing import List, Optional

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.book.author import Author
from src.common.schemas.book.author import AuthorsDTO, AuthorInDB
from src.common.converts.author import convert_author_model_to_dto


class AuthorRepositories(CRUDBase):
    model = Author

    async def get_author(self, author_id: int) -> Optional[AuthorInDB]:
        result = await self._get(field=self.model.id, value=author_id)
        return convert_author_model_to_dto(result)

    async def get_list_authors(self, limit: int = 20,
                               offset: int = 0
                               ) -> Optional[List[AuthorInDB]]:
        result = await self._get_list(limit, offset)
        total = [convert_author_model_to_dto(i) for i in result]
        return total

    async def create_author(self, data: AuthorsDTO) -> AuthorInDB:
        result = await self._create(data.__dict__)
        return convert_author_model_to_dto(result)

    async def update_author(self, data: AuthorsDTO, author_id: int) -> AuthorInDB:
        result = await self._update(field=self.model.id, value=author_id, data=data.__dict__)
        return convert_author_model_to_dto(result)
