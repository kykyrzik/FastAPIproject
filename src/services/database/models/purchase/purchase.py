from datetime import datetime
from typing import List
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import TIMESTAMP

from src.services.database.models.base import Base


class Purchase(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    delivery_address: Mapped[str] = mapped_column(nullable=False)
    purchase_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    price: Mapped[Decimal] = mapped_column(nullable=False)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    item: Mapped[List["Item"]] = relationship(back_populates="purchase")
    user: Mapped["User"] = relationship(back_populates="purchase")
