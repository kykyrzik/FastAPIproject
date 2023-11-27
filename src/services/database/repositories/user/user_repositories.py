from typing import Optional, ClassVar, Type

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.user.user import User
from src.common.schemas.user.user import UserCreateDTO,  UpdateUsername, UserInDB
from src.services.security import secturity
from src.common.converts.user import convert_author_model_to_dto


class UserRepositories(CRUDBase):
    model: ClassVar[Type[User]] = User

    async def create_user(self, data: UserCreateDTO) -> Optional[UserInDB]:
        new_user = data.__dict__
        password = new_user.pop("password")
        new_user["hashed_password"] = secturity.get_password_hash(password)
        result = await self._create(data=new_user)
        return convert_author_model_to_dto(result)

    async def delete_user(self, user_id: int) -> bool:
        return await self._delete(field=self.model.id, model_id=user_id)

    async def update_user(self, user_id: int, data: UpdateUsername) -> UserInDB:
        result = await self._update(field=self.model.id, value=user_id, data=data.__dict__)
        return convert_author_model_to_dto(result)
