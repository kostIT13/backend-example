# tests/integration/test_users_async.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_users_async(async_client: AsyncClient):
    """Асинхронный тест: получение списка пользователей"""
    response = await async_client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_user_async(async_client: AsyncClient, test_user_data):
    """Асинхронный тест: создание пользователя"""
    response = await async_client.post("/users", json=test_user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_user_data["name"]