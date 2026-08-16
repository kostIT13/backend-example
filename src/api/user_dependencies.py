from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db.database import get_db
from src.services.user_service.repository import UserRepository

async def get_user_repository(
    session: AsyncSession = Depends(get_db)
) -> UserRepository:
    """
    DI-зависимость для репозитория пользователей.
    FastAPI создаёт сессию, передаёт её в репозиторий.
    """
    return UserRepository(session)

# Тип для использования в эндпоинтах
from typing import Annotated
UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]