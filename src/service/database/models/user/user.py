from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.service.database.models.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_passowrd: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
