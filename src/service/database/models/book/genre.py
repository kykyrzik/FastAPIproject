from sqlalchemy import Column, String, Integer

from src.service.database.models.base import Base


class Genre(Base):
    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String, nullable=False, unique=True)
