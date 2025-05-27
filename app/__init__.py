from flask import Flask
from flask_migrate import Migrate
from config import Config
from .db import db
from .routes import register_blueprints

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.models import user, file, logs

    migrate.init_app(app, db)

    register_blueprints(app)

    return app
