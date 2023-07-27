import unittest
from flask import Flask
from unittest.mock import MagicMock
from app.models.user_model import User
from app.controllers.user_controller import user_controller


class TestUserController(unittest.TestCase):
    def setUp(self):
        # Set up the Flask application and test client
        app = Flask(__name__)
        app.register_blueprint(user_controller)
        self.app = app.test_client()

        # Create a mock UserService and inject it into the controller
        self.mock_user_service = MagicMock()
        app.before_request(self.inject_mock_dependencies)

    def tearDown(self):
        pass

    def inject_mock_dependencies(self):
        from flask import g
        g.user_service = self.mock_user_service

    def test_get_users(self):
        self.mock_user_service.get_all_users.return_value = [
            User(1, "John Doe", "johndoe@example.com"),
            User(2, "Jane Smith", "janesmith@example.com")
        ]

        response = self.app.get('/users')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_user(self):
        self.mock_user_service.get_user_by_id.return_value = User(1, "John Doe", "johndoe@example.com")

        response = self.app.get('/users/1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")

    def test_create_user(self):
        user_data = {"name": "Alice", "email": "alice@example.com"}
        self.mock_user_service.create_user.return_value = User(3, "Alice", "alice@example.com")

        response = self.app.post('/users', json=user_data)
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["name"], "Alice")

    def test_update_user(self):
        user_id = 1
        user_data = {"name": "Updated Name", "email": "updated@example.com"}
        self.mock_user_service.update_user.return_value = User(user_id, "Updated Name", "updated@example.com")

        response = self.app.put(f'/users/{user_id}', json=user_data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Updated Name")

    def test_delete_user(self):
        user_id = 1
        self.mock_user_service.delete_user.return_value = True

        response = self.app.delete(f'/users/{user_id}')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "User deleted")


if __name__ == '__main__':
    unittest.main()
