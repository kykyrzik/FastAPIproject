from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.services.database.models.base import Base


class Item(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    book_id: Mapped[str] = mapped_column(ForeignKey("book.ISBN", ondelete="CASCADE"), nullable=False)
    amount_item: Mapped[int] = mapped_column(default=1)

    book: Mapped["Book"] = relationship(back_populates="item")
    purchase: Mapped["Purchase"] = relationship(back_populates="item")
