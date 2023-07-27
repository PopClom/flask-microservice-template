import unittest
from app.repositories.user_repository import UserRepository
from app.models.user_model import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        mock_users = [
            User(id=1, name="John Doe", email="johndoe@example.com"),
            User(id=2, name="Jane Smith", email="janesmith@example.com")
        ]
        self.user_repository = UserRepository()
        self.user_repository.users = mock_users

    def tearDown(self):
        pass

    def test_get_all_users(self):
        users = self.user_repository.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "John Doe")
        self.assertEqual(users[1].name, "Jane Smith")

    def test_get_user_by_id(self):
        user_id = 1
        user = self.user_repository.get_user_by_id(user_id)

        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@example.com")

    def test_create_user(self):
        user_data = {"name": "Alice", "email": "alice@example.com"}

        created_user = self.user_repository.create_user(user_data)

        self.assertIsNotNone(created_user.id)
        self.assertEqual(created_user.name, "Alice")
        self.assertEqual(created_user.email, "alice@example.com")

    def test_update_user(self):
        user_id = 1
        user_data = {"name": "Updated Name", "email": "updated@example.com"}

        updated_user = self.user_repository.update_user(user_id, user_data)

        self.assertEqual(updated_user.id, 1)
        self.assertEqual(updated_user.name, "Updated Name")
        self.assertEqual(updated_user.email, "updated@example.com")

    def test_delete_user(self):
        mock_users = [
            User(id=1, name="John Doe", email="johndoe@example.com"),
            User(id=2, name="Jane Smith", email="janesmith@example.com")
        ]
        self.user_repository.users = mock_users

        user_id = 1
        result = self.user_repository.delete_user(user_id)

        self.assertTrue(result)
        self.assertEqual(len(self.user_repository.users), 1)


if __name__ == '__main__':
    unittest.main()
