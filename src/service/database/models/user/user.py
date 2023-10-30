from sqlalchemy import Column, String, Integer

from src.service.database.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    hashed_passowrd = Column(String, nullable=False)
    username = Column(String, nullable=False)
