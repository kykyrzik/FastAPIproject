from datetime import timedelta
from typing import Optional, ClassVar, Type
from fastapi import HTTPException

from src.services.database.repositories.base import CRUDBase
from src.services.database.models.user.user import User
from src.common.schemas.user.user import UserCreateDTO,  UpdateUsername, UserInDB
from src.services.security import secturity
from src.common.converts.user import convert_user_model_to_dto
from src.services.security.JWT import create_access_token


class UserRepositories(CRUDBase):
    model: ClassVar[Type[User]] = User

    async def create_user(self, data: UserCreateDTO) -> Optional[UserInDB]:
        new_user = data.__dict__
        password = new_user.pop("password")
        new_user["hashed_password"] = secturity.get_password_hash(password)
        result = await self._create(data=new_user)
        return convert_user_model_to_dto(result)

    async def get(self, email: str) -> Optional[UserInDB]:
        return convert_user_model_to_dto(await self._get(field=self.model.email, value=email))

    async def authenticate(self, email: str, password: str) -> dict[str, str]:
        user = await self.get(email=email)
        if not user or not secturity.verify_password(password, user.password):
            raise HTTPException(status_code=404, detail="incorrect email or password")
        if user.is_active:
            raise HTTPException(status_code=401, detail="Inactive user")
        access_token_minute = timedelta(minutes=30)
        return {"access_token": create_access_token(
                    data={"sub": {
                        "password": password,
                        "email": email}
                    },
                    expires_delta=access_token_minute),
                "token_type": "bearer"
                }

    async def activate_user(self, user_id: int) -> UserInDB | bool:
        data = {'is_active': True}
        return await self._update(
                                field=self.model.id,
                                value=user_id,
                                data=data
                                )

    async def is_active(self, user: UserInDB) -> bool:
        return user.is_active

    async def delete_user(self, user_id: int) -> bool:
        return await self._delete(field=self.model.id, model_id=user_id)

    async def update_user(self, user_id: int, data: UpdateUsername) -> UserInDB:
        result = await self._update(field=self.model.id, value=user_id, data=data.__dict__)
        return convert_user_model_to_dto(result)
