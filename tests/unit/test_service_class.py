import pytest
from src.services.user_service.service import UserService
from src.services.user_service.repository import UserRepository

def test_user_service_with_mock_repository(mocker):
    """Тест: мокаем репозиторий и передаём его в сервис"""
    
    # Создаём мок репозитория
    mock_repo = mocker.Mock(spec=UserRepository)
    
    # Настраиваем поведение мока
    mock_repo.get_all.return_value = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"}
    ]
    
    # Создаём сервис с мок-репозиторием
    service = UserService(mock_repo)
    
    # Вызываем метод
    users = service.get_all_users()
    
    # Проверяем результат
    assert len(users) == 2
    assert users[0]["name"] == "User 1"
    
    # Проверяем, что мок был вызван
    mock_repo.get_all.assert_called_once()