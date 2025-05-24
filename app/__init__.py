# app/__init__.py
from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 블루프린트 등록
    from .main import main as main_bp
#    app.register_blueprint(main_bp)
    app.register_blueprint(main_bp, url_prefix='/main')
    return app

