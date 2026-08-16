from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, Dict, Any

# Тип для модели (будет подставляться при наследовании)
ModelType = TypeVar("ModelType")

class BaseRepository(ABC, Generic[ModelType]):
    """
    Базовый интерфейс для всех репозиториев.
    Определяет стандартные CRUD-операции.
    """
    
    @abstractmethod
    async def get_all(self) -> List[ModelType]:
        """Получить все записи"""
        pass
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[ModelType]:
        """Получить запись по ID"""
        pass
    
    @abstractmethod
    async def create(self, **kwargs) -> ModelType:
        """Создать запись"""
        pass
    
    @abstractmethod
    async def update(self, id: int, **kwargs) -> Optional[ModelType]:
        """Обновить запись"""
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> bool:
        """Удалить запись"""
        pass