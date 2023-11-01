from sqlalchemy import (Column,
                        Integer,
                        String,
                        Date,
                        ForeignKey,
                        )

from sqlalchemy.orm import relationship
from src.service.database.models.base import Base


class Purchase(Base):
    id = Column(Integer, primary_key=True, index=True)
    delivery_address = Column(String, nullable=False)
    purchase_date = Column(Date)

    item_id = Column(Integer, ForeignKey("item.py", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    item = relationship("Item", back_populates="purchases")
    user = relationship("User", back_populates="puerchase")
