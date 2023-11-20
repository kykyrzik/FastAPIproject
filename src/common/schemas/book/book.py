from typing import Optional
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy.types import BLOB


class UpdateBookDTO(BaseModel):
    name_book: str
    author_id: int
    genre_id: int
    unit_price: Decimal
    amount_book: int


class BookDTO(UpdateBookDTO):
    ISBN: str
    publication_date: Optional[datetime] = None
    book_circulation: Optional[int] = None
    weight: Optional[int]
    rars_id: int
    number_of_pages: int
    cover_type_id: int
    images: Optional[BLOB] = None
