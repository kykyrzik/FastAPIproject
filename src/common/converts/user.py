from src.services.database.models.user.user import User
from src.common.schemas.user.user import UserInDB


def convert_author_model_to_dto(author: User) -> UserInDB:
    return UserInDB(id=author.id,
                    email=author.email,
                    username=author.username
                    )
