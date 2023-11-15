from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.service.database.models.base import Base


class Author(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    fullname_author: Mapped[str] = mapped_column(nullable=False, unique=True)
