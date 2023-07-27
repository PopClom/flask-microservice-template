import unittest
from app.services.user_service import UserService
from app.models.user_model import User
from unittest.mock import MagicMock


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_user_repository = MagicMock()
        self.mock_email_client = MagicMock()
        self.user_service = UserService(self.mock_user_repository, self.mock_email_client)

    def tearDown(self):
        pass

    def test_get_all_users(self):
        self.mock_user_repository.get_all_users.return_value = [
            User(id=1, name="John Doe", email="johndoe@example.com"),
            User(id=2, name="Jane Smith", email="janesmith@example.com")
        ]

        users = self.user_service.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "John Doe")
        self.assertEqual(users[1].name, "Jane Smith")

    def test_get_user_by_id(self):
        self.mock_user_repository.get_user_by_id.return_value = User(id=1, name="John Doe", email="johndoe@example.com")

        user = self.user_service.get_user_by_id(1)

        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@example.com")

    def test_create_user(self):
        user_data = {"name": "Alice", "email": "alice@example.com"}

        self.mock_user_repository.create_user.return_value = User(id=3, name="Alice", email="alice@example.com")
        self.mock_email_client.send_registration_email.return_value = {}

        created_user = self.user_service.create_user(user_data)

        self.assertEqual(created_user.name, "Alice")
        self.assertEqual(created_user.email, "alice@example.com")
        self.mock_email_client.send_registration_email.assert_called()

    def test_update_user(self):
        user_id = 1
        user_data = {"name": "Updated Name", "email": "updated@example.com"}

        self.mock_user_repository.update_user.return_value = User(id=user_id, name="Updated Name",
                                                                  email="updated@example.com")

        updated_user = self.user_service.update_user(user_id, user_data)

        self.assertEqual(updated_user.name, "Updated Name")
        self.assertEqual(updated_user.email, "updated@example.com")

    def test_delete_user(self):
        user_id = 1

        self.mock_user_repository.delete_user.return_value = True

        result = self.user_service.delete_user(user_id)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
