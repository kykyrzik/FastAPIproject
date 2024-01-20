from src.services.database.models.book.book import Book
from src.common.schemas.book.book import BookDTO


def convert_book_model_to_dto(book: Book) -> BookDTO:
    return BookDTO(ISBN=book.ISBN,
                   author_id=book.author_id,
                   name_book=book.name_book,
                   genre_id=book.genre_id,
                   unit_price=book.unit_price,
                   amount_book=book.amount_book,
                   publication_date=book.publication_date,
                   book_circulation=book.book_circulation,
                   weight=book.weight,
                   rars=book.rars,
                   number_of_pages=book.number_of_pages,
                   cover_type=book.cover_type,
                   publisher=book.publisher)
