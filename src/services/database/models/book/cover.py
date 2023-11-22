from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.services.database.models.base import Base


class Cover(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cover_type: Mapped[str] = mapped_column(nullable=False, unique=True)

    book: Mapped["Book"] = relationship(back_populates="cover")
