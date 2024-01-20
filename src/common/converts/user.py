from src.services.database.models.user.user import User
from src.common.schemas.user.user import UserInDB


def convert_user_model_to_dto(user: User) -> UserInDB:
    return UserInDB(id=user.id,
                    email=user.email,
                    username=user.username,
                    is_admin=user.is_admin,
                    password=user.hashed_password,
                    is_active=user.is_active
                    )
