import os
from flask import g
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.clients.email_client import EmailClient

# Singleton instance of UserService
_user_service_instance = None


def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        from config import ProdConfig
        return ProdConfig
    else:
        from config import DevConfig
        return DevConfig


def get_user_service():
    global _user_service_instance

    if 'user_service' not in g:
        if _user_service_instance is None:
            user_repository = UserRepository()
            email_client = EmailClient(get_config().EMAIL_CLIENT_URL)
            _user_service_instance = UserService(user_repository, email_client)

        g.user_service = _user_service_instance
    return g.user_service
