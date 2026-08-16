import pytest
from src.api.dependencies import get_user_service
from httpx import AsyncClient

class MockUserService:
    def get_all(self):
        return [{"id": 999, "name": "Mock User"}]

def mock_get_user_service():
    return MockUserService()

@pytest.mark.asyncio
async def test_get_users_with_mock(async_client: AsyncClient):
    # Подменяем зависимость
    from src.main import app
    app.dependency_overrides[get_user_service] = mock_get_user_service
    
    response = await async_client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["id"] == 999
    assert data[0]["name"] == "Mock User"
    
    # Восстанавливаем оригинальную зависимость
    app.dependency_overrides.clear()