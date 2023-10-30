from sqlalchemy import Column, String, Integer

from src.service.database.models.base import Base


class Authors(Base):
    id = Column(Integer, primary_key=True, index=True)
    fullname_author = Column(String, nullable=False, unique=True)
