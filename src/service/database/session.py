from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.setting import load_settings


engine = create_async_engine(load_settings().DB_URL, echo=True)

assync_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with assync_session_maker() as session:
        yield session
