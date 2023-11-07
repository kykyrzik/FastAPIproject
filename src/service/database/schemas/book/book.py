from typing import Optional
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy.types import BLOB


class BookDTO(BaseModel):
    ISBN: str
    name_book: str
    author_id: int
    genre_id: int
    publication_date: Optional[datetime] = None
    book_circulation: Optional[int] = None
    unit_price: Decimal
    weight: Optional[int]
    rars_id: int
    number_of_pages: int
    cover_type_id: int
    images: Optional[BLOB]
    amount_book: int
