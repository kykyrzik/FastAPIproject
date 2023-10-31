from sqlalchemy import (Column,
                        VARCHAR,
                        Integer,
                        ForeignKey,
                        Date,
                        DECIMAL,
                        BLOB)

from sqlalchemy.orm import relationship
from src.service.database.models.base import Base


class Book(Base):
    ISBN = Column(VARCHAR(17), primary_key=True)
    name_book = Column(VARCHAR(50), index=True)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    publication_date = Column(Date, nullable=True)
    book_circulation = Column(Integer, nullable=True)
    unit_price = Column(DECIMAL(4, 2), nullable=False)
    weight = Column(Integer)  # in grams
    rars_id = Column(Integer, ForeignKey("rars.id", ondelete="CASCADE"), nullable=False)
    number_of_pages = Column(Integer, nullable=False)
    cover_type_id = Column(Integer, ForeignKey("cover_type.id", ondelete="CASCADE"), nullable=False)
    images = Column(BLOB)
    amount_book = Column(Integer, nullable=False)

    author = relationship("Author", back_populates="book")
    genre = relationship("Genre", back_populates="book")
    rars = relationship("RARS", back_populates="book")
    cover_type = relationship("CoverType", back_populates="book")
