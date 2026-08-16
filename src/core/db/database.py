from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.core.config import settings
from typing import AsyncGenerator

# Создаём асинхронный Engine
async_engine = create_async_engine(
    settings.database_url,      # PostgreSQL URL
    echo=settings.debug,        # Логировать SQL-запросы (только для разработки)
    pool_size=10,               # Максимум соединений в пуле
    max_overflow=20,            # Дополнительные соединения при нагрузке
)

AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,   # Объекты остаются доступными после коммита
    autocommit=False,
    autoflush=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()