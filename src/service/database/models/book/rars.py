from sqlalchemy import Column, Integer, VARCHAR

from src.service.database.models.base import Base


class RARS(Base):
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(VARCHAR(3), nullable=False, unique=True)
