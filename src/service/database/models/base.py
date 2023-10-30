from typing import Any

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):
    id: Any

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
