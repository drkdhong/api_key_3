import os
from flask import Flask
from config import config  # config는 dict여야 함

def create_app():
    app = Flask(__name__)
    config_name = os.environ.get("CONFIG", "local")
    app.config.from_object(config[config_name])

    from main.views import main
    app.register_blueprint(main)
    return app

