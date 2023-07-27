class Config:
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    EMAIL_CLIENT_URL = 'https://dev.example.com'
    # Add other development-specific configuration variables here


class ProdConfig(Config):
    EMAIL_CLIENT_URL = 'https://prod.example.com'
    # Add production-specific configuration variables here
