from flask import Flask
from config import Config
from .db import db
from .routes import register_blueprints


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_blueprints(app)

    return app
