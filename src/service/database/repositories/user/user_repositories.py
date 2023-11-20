from typing import Optional

from src.service.database.repositories.base import CRUDBase
from src.service.database.models.user.user import User
from src.common.schemas.user.user import UserCreateDTO,  UpdateUsername, UserInDB
from src.service.security import secturity


class UserRepositories(CRUDBase):
    model = User

    async def create_user(self, data: UserCreateDTO) -> Optional[UserInDB]:
        new_user = data.__dict__
        password = new_user.pop("passsword")
        new_user["password"] = secturity.get_password_hash(password)
        return await self._create(data=new_user)

    async def delete_user(self, user_id: int) -> bool:
        return await self._delete(field=self.model, model_id=user_id)

    async def update_user(self, user_id: int, data: UpdateUsername) -> UserInDB:
        data = data.__dict__
        return await self._update(field=self.model, value=user_id, data=data)
