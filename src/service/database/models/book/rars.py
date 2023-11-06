from sqlalchemy.types import SMALLINT, VARCHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.service.database.models.base import Base


class RARS(Base):
    id: Mapped[int] = mapped_column(SMALLINT, primary_key=True, index=True)
    rating: Mapped[str] = mapped_column(VARCHAR(3), nullable=False, unique=True)
