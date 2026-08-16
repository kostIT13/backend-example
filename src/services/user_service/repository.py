from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import Optional, List

from src.services.user_service.base import BaseRepository
from src.core.db.models import User

class UserRepository(BaseRepository[User]):
    """
    Репозиторий для работы с моделью User.
    Реализует все методы базового интерфейса.
    """
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_all(self) -> List[User]:
        """Получить всех пользователей"""
        result = await self.session.execute(select(User))
        return result.scalars().all()
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        """Получить пользователя по ID"""
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """Получить пользователя по email (специфичный метод)"""
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def create(self, **kwargs) -> User:
        """Создать нового пользователя"""
        user = User(**kwargs)
        self.session.add(user)
        await self.session.flush()  # Отправляем в БД, но не коммитим
        return user
    
    async def update(self, user_id: int, **kwargs) -> Optional[User]:
        """Обновить пользователя"""
        user = await self.get_by_id(user_id)
        if not user:
            return None
        
        # Обновляем только переданные поля
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        await self.session.flush()
        return user
    
    async def delete(self, user_id: int) -> bool:
        """Удалить пользователя"""
        user = await self.get_by_id(user_id)
        if not user:
            return False
        
        await self.session.delete(user)
        await self.session.flush()
        return True
    
    async def get_active_users(self) -> List[User]:
        """Получить активных пользователей (специфичный метод)"""
        result = await self.session.execute(
            select(User).where(User.is_active == True)
        )
        return result.scalars().all()