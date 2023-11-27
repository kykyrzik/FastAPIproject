from src.services.database.models.book.author import Author
from src.common.schemas.book.author import AuthorInDB


def convert_author_model_to_dto(author: Author) -> AuthorInDB:
    return AuthorInDB(id=author.id,
                      name=author.name,
                      surname=author.surname
                      )

