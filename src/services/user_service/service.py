
class UserService:
    def get_user(self, user_id: int):
        if user_id < 1:
            raise ValueError("User ID must be > 0")
        # Этот блок не протестирован!
        if user_id > 100:
            return {"error": "User not found"}
        return {"id": user_id, "name": f"User {user_id}"}