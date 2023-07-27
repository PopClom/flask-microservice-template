from app.models.user_model import User


class UserRepository:
    def __init__(self):
        self.users = [
            User(1, "John Doe", "johndoe@example.com"),
            User(2, "Jane Smith", "janesmith@example.com")
        ]

    def get_all_users(self) -> list[User]:
        return [user for user in self.users]

    def get_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create_user(self, user_data: dict[str, str]) -> User:
        new_user = User(len(self.users) + 1, user_data["name"], user_data["email"])
        self.users.append(new_user)
        return new_user

    def update_user(self, user_id: int, user_data: dict[str, str]) -> User | None:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = user_data.get("name", user.name)
            user.email = user_data.get("email", user.email)
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
