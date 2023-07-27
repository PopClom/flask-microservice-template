from flask import Flask
from bootstrap import get_config
from app.controllers.user_controller import user_controller


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    app.register_blueprint(user_controller, url_prefix='/api')
    return app
