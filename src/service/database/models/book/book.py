from datetime import datetime
from typing import Optional

from sqlalchemy import (VARCHAR,
                        DECIMAL,
                        BLOB,
                        ForeignKey)

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.service.database.models.base import Base
from src.service.database.models import book as b


class Book(Base):
    ISBN: Mapped[str] = mapped_column(VARCHAR(17), primary_key=True)
    name_book: Mapped[str] = mapped_column(VARCHAR(50), index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    publication_date: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    book_circulation: Mapped[Optional[int]] = mapped_column(nullable=True)
    unit_price: Mapped[float] = mapped_column(DECIMAL(4, 2), nullable=False)
    weight: Mapped[Optional[int]]  # in grams
    rars_id: Mapped[int] = mapped_column(ForeignKey("rars.id", ondelete="CASCADE"), nullable=False)
    number_of_pages: Mapped[int] = mapped_column(nullable=False)
    cover_type_id: Mapped[int] = mapped_column(ForeignKey("cover_type.id", ondelete="CASCADE"), nullable=False)
    images: Mapped[Optional[BLOB]]
    amount_book: Mapped[int] = mapped_column(nullable=False)

    author: Mapped["b.author.Author"] = relationship(back_populates="book")
    genre: Mapped["b.genre.Genre"] = relationship(back_populates="book")
    rars: Mapped["b.rars.RARS"] = relationship(back_populates="book")
    cover_type: Mapped["b.cover_type.CoverType"] = relationship(back_populates="book")
