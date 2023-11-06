from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import TIMESTAMP

from src.service.database.models.base import Base
from src.service.database.models import item as i, user as u


class Purchase(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    delivery_address: Mapped[str] = mapped_column(nullable=False)
    purchase_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    item_id: Mapped[int] = mapped_column(ForeignKey("item.py", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    item: Mapped["i.Item"] = relationship(back_populates="purchases")
    user: Mapped["u.User"] = relationship(back_populates="puerchase")
