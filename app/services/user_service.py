from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.clients.email_client import EmailClient


class UserService:
    def __init__(self, user_repository: UserRepository, email_client: EmailClient) -> None:
        self.user_repository = user_repository
        self.email_client = email_client

    def get_all_users(self) -> list[User]:
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user_data: dict[str, str]) -> User:
        new_user = self.user_repository.create_user(user_data)
        if new_user is not None:
            self.email_client.send_registration_email(new_user.email)
        return new_user

    def update_user(self, user_id: int, user_data: dict[str, str]) -> User | None:
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete_user(user_id)
