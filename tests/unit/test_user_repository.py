import pytest
from src.services.user_service.repository import UserRepository
from tests.unit.test_user_repository_mock import MockUserRepository

@pytest.mark.asyncio
async def test_get_users():
    """Тест: получение пользователей через мок-репозиторий"""
    # Подменяем реальный репозиторий на мок
    repo = MockUserRepository()
    
    users = await repo.get_all()
    assert len(users) == 1
    assert users[0].name == "Test User"

@pytest.mark.asyncio
async def test_create_user():
    """Тест: создание пользователя через мок-репозиторий"""
    repo = MockUserRepository()
    
    user = await repo.create(name="New User", email="new@example.com")
    assert user.id == 2
    assert user.name == "New User"
    
    users = await repo.get_all()
    assert len(users) == 2