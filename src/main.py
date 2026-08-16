from fastapi import FastAPI
from src.api.routers.health_routers import router as health_routers
from src.api.routers.users_routers import router as user_routers

# 1. Создаём экземпляр приложения
app = FastAPI(title="My API", version="0.1.0")

app.include_router(health_routers)
app.include_router(user_routers)

# 2. Корневой эндпоинт
@app.get("/")
async def root():
    return {"message": "Hello, World!"}
