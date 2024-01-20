from src.services.database.models.book.genre import Genre
from src.common.schemas.book.genre import GenreInDB


def convert_genre_model_to_dto(genre_obj: Genre) -> GenreInDB:
    return GenreInDB(id=genre_obj.id,
                     genre=genre_obj.genre
                     )
