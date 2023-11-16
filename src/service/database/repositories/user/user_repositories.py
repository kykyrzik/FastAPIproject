from typing import Optional

from src.service.database.repositories.base import CRUDBase
from src.service.database.models.user.user import User
from src.service.database.schemas.user.user import UserCreateDTO, UserBase, UpdateUsername


class UserRepositories(CRUDBase):
    model = User

    async def get(self, user_id: int = None) -> UserBase:
        return await self._get(field=self.model, value=user_id)

    async def create_user(self, data: UserCreateDTO) -> Optional[UserCreateDTO]:
        new_user = data.__dict__
        password = new_user.pop("passsword")
        new_user["password"] = hashed_password(password)  # temp stub
        return await self._create(data=new_user)

    async def delete_user(self, user_id: int) -> bool:
        return await self._delete(field=self.model, model_id=user_id)

    async def update_user(self, user_id: int, data: UpdateUsername) -> UserBase:
        data = data.__dict__
        return await self._update(field=self.model, value=user_id, data=data)
