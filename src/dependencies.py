# src/api/dependencies.py
from src.services.user_service.service import UserService
from src.services.user_service.repository import UserRepository
from fastapi import Depends

def get_user_repository() -> UserRepository:
    return UserRepository()

def get_user_service(
    repo: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(repo)