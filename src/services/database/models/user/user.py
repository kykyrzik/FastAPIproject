from typing import Set

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from src.services.database.models.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)

    purchase: Mapped[Set["Purchase"]] = relationship(back_populates="user")
