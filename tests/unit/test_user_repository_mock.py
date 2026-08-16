from src.services.user_service.repository import UserRepository
from src.core.db.models import User

class MockUserRepository:
    """Мок-репозиторий для тестов (без реальной БД)"""
    
    def __init__(self):
        self.users = [
            User(id=1, name="Test User", email="test@example.com")
        ]
        self._next_id = 2
    
    async def get_all(self):
        return self.users
    
    async def get_by_id(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    async def get_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    async def create(self, **kwargs):
        user = User(id=self._next_id, **kwargs)
        self._next_id += 1
        self.users.append(user)
        return user
    
    async def update(self, user_id: int, **kwargs):
        user = await self.get_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        return user
    
    async def delete(self, user_id: int):
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False

    