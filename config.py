import os
from pathlib import Path

# Create a directory for the SQLite database if it doesn't exist
DB_DIR = Path(__file__).parent / "instance"
DB_DIR.mkdir(exist_ok=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-please-change")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_DIR}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
