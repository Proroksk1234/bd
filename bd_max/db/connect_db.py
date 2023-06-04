from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from bd_max.configurate.config import SQLALCHEMY_DATABASE_URL

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True)
Base = declarative_base()
async_session = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
