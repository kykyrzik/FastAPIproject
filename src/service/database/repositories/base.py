from typing import TypeVar, ClassVar, Optional, Type, Any
from abc import ABC

from sqlalchemy import select, update, delete
from sqlalchemy.orm.exc import NoResultFound

from src.service.database.session import AsyncSession
from src.service.database.models.base import Base

Model = TypeVar("Model", bound=Base)


class CRUDBase(ABC):
    model: ClassVar[Type[Model]]

    def __init__(self, session: AsyncSession):
        self._session = session

    async def _create(self, data: dict) -> Optional[Model]:
        new_obj = self.model(**data)
        self._session.add(new_obj)
        await self._session.commit()
        await self._session.refresh(new_obj)
        return new_obj

    async def _get(self, field: Any, value: Any) -> Optional[Model]:
        try:
            stmt = (select(self.model)
                    .where(value == field)
                    )
            result = await self._session.execute(stmt).scalar()
            return result
        except NoResultFound:
            return None

    async def _update(self, field: Any, value: Any, data: dict) -> Optional[Model]:
        stmt = (update(self.model).
                where(field == value).
                values(**data).
                returnig(self.model))
        result = await self._session.execute(stmt).scalar()
        return result

    async def _delete(self, field: Any, model_id: int) -> bool:
        stmt = (
            delete(self.model).
            where(field == model_id)
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        if result.rowcount:
            return True
        return False
