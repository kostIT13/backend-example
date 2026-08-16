import pytest
from src.services.user_service.service import UserService

def test_get_user_with_mock(mocker):
    """
    Тест: мокаем метод get_user_from_db
    """
    # Создаём экземпляр сервиса
    service = UserService()
    
    # Мокаем метод get_user_from_db
    mock_get_user = mocker.patch.object(service, 'get_user_from_db')
    mock_get_user.return_value = {"id": 1, "name": "Mock User"}
    
    # Вызываем метод, который использует мок
    result = service.get_user(1)
    
    # Проверяем результат
    assert result["name"] == "Mock User"
    
    # Проверяем, что мок был вызван с правильным аргументом
    mock_get_user.assert_called_once_with(1)