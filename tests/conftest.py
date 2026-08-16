# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from src.main import app

@pytest.fixture
def client():
    """Создаёт синхронный тестовый клиент FastAPI"""
    return TestClient(app)

@pytest.fixture
async def async_client():
    """Создаёт асинхронный тестовый клиент FastAPI"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
def test_user_data():
    """Возвращает тестовые данные пользователя"""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpassword123"
    }