import pytest
from fastapi.testclient import TestClient

def test_get_users(client: TestClient):
    """Тест: получение списка пользователей"""
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user(client: TestClient, test_user_data):
    """Тест: создание пользователя"""
    response = client.post("/users", json=test_user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_user_data["name"]
    assert data["email"] == test_user_data["email"]