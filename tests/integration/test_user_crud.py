import pytest
from httpx import AsyncClient

class TestUserCRUD:
    """Тесты CRUD-операций для пользователей"""
    
    @pytest.mark.asyncio
    async def test_full_user_flow(self, async_client: AsyncClient, test_user_data):
        """
        Полный сценарий: создание → получение → обновление → удаление
        """
        # 1. Создаём пользователя
        create_response = await async_client.post("/users", json=test_user_data)
        assert create_response.status_code == 201
        user = create_response.json()
        user_id = user["id"]
        
        # 2. Получаем пользователя
        get_response = await async_client.get(f"/users/{user_id}")
        assert get_response.status_code == 200
        assert get_response.json()["name"] == test_user_data["name"]
        
        # 3. Обновляем пользователя
        update_data = {"name": "Updated Name"}
        update_response = await async_client.put(f"/users/{user_id}", json=update_data)
        assert update_response.status_code == 200
        assert update_response.json()["name"] == "Updated Name"
        
        # 4. Удаляем пользователя
        delete_response = await async_client.delete(f"/users/{user_id}")
        assert delete_response.status_code == 204
        
        # 5. Проверяем, что пользователь удалён
        get_response = await async_client.get(f"/users/{user_id}")
        assert get_response.status_code == 404