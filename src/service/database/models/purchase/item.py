from sqlalchemy import Column, Integer, ForeignKey, VARCHAR

from sqlalchemy.orm import relationship

from src.service.database.models.base import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(VARCHAR(17), ForeignKey("book.ISBN", ondelete="CASCADE"), nullable=False)
    amount_item = Column(Integer, default=1)

    book = relationship("Book", back_populates="item")
