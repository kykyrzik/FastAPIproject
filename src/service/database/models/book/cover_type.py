from sqlalchemy import Column, String, Integer

from src.service.database.models.base import Base


class CoverType(Base):
    id = Column(Integer, primary_key=True, index=True)
    cover_type = Column(String, nullable=False, unique=True)
