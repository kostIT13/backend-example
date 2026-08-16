from fastapi import APIRouter, HTTPException

# 1. Создаём роутер с префиксом и тегом
router = APIRouter(prefix="/users", tags=["users"])

# 2. Временное хранилище (пока без БД)
users_db = {}
user_id_counter = 1

# 3. Эндпоинты регистрируются через router, а не через app
@router.get("/")
async def get_users():
    return list(users_db.values())

@router.get("/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.post("/", status_code=201)
async def create_user(name: str, email: str):
    global user_id_counter
    
    for existing_user in users_db.values():
        if existing_user["email"] == email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = user_id_counter
    user_id_counter += 1
    
    new_user = {
        "id": user_id,
        "name": name,
        "email": email,
        "is_active": True
    }
    users_db[user_id] = new_user
    
    return new_user

@router.put("/{user_id}")
async def update_user(user_id: int, name: str, email: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    current_user = users_db[user_id]
    
    for existing_user in users_db.values():
        if existing_user["email"] == email and existing_user["id"] != user_id:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    current_user["name"] = name
    current_user["email"] = email
    
    return current_user

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    del users_db[user_id]
    return None