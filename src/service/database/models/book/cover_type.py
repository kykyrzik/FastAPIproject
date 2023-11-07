from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import SMALLINT

from src.service.database.models.base import Base


class Cover(Base):
    id: Mapped[int] = mapped_column(SMALLINT, primary_key=True, index=True)
    cover_type: Mapped[str] = mapped_column(nullable=False, unique=True)
