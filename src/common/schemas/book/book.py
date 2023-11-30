from typing import Optional
import re

from pydantic import BaseModel, field_validator, condecimal


class ValidationISBN(BaseModel):
    ISBN: str

    @field_validator("ISBN")
    @classmethod
    def validate_by_regexp(cls, isbn: str) -> str:
        pattern = '^(?:ISBN(?:-13)?:?\ )?(?=[0-9]{13}$|(?=(?:-?3(?:-?16)?-?)?)(?:\d+-?){5}$)[0-9-]+$'
        if re.match(pattern, isbn) is None:
            return ValueError("ISBN is not incorrect format")
        return isbn


class UpdateBookDTO(BaseModel):
    name_book: str
    author_id: int
    genre_id: int
    unit_price: condecimal(max_digits=6, decimal_places=2)
    amount_book: int


class BookDTO(ValidationISBN, UpdateBookDTO):
    publication_date: Optional[int] = None
    book_circulation: Optional[int] = None
    weight: Optional[int]
    rars: str
    number_of_pages: int
    cover_type: str
    publisher: str
