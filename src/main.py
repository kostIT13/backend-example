from fastapi import FastAPI

# 1. Создаём экземпляр приложения
app = FastAPI(title="My API", version="0.1.0")

# 2. Корневой эндпоинт
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# 3. Эндпоинт для проверки здоровья
@app.get("/health")
async def health_check():
    return {"status": "healthy"}