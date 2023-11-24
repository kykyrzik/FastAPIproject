from typing import Optional
from decimal import Decimal

from sqlalchemy import (VARCHAR,
                        DECIMAL,
                        ForeignKey,
                        )

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.services.database.models.base import Base


class Book(Base):
    ISBN: Mapped[str] = mapped_column(VARCHAR(17), primary_key=True)
    name_book: Mapped[str] = mapped_column(VARCHAR(50), index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    publisher_id: Mapped[int] = mapped_column(ForeignKey("publisher.id", ondelete="CASCADE"), nullable=False)
    publication_date: Mapped[Optional[int]] = mapped_column(nullable=True)
    book_circulation: Mapped[Optional[int]] = mapped_column(nullable=True)
    unit_price: Mapped[Decimal] = mapped_column(DECIMAL(6, 2), nullable=False)
    weight: Mapped[Optional[int]]  # in grams
    rars_id: Mapped[int] = mapped_column(ForeignKey("rars.id", ondelete="CASCADE"), nullable=False)
    number_of_pages: Mapped[int] = mapped_column(nullable=False)
    cover_type_id: Mapped[int] = mapped_column(ForeignKey("cover.id", ondelete="CASCADE"), nullable=False)
    amount_book: Mapped[int] = mapped_column(nullable=False)

    author: Mapped["Author"] = relationship(back_populates="book")
    genre: Mapped["Genre"] = relationship(back_populates="book")
    rars: Mapped["RARS"] = relationship(back_populates="book")
    cover: Mapped["Cover"] = relationship(back_populates="book")
    publisher: Mapped["Publisher"] = relationship(back_populates="book")
    item: Mapped["Item"] = relationship(back_populates="book")
