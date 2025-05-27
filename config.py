import os
from pathlib import Path

# Create a directory for the SQLite database if it doesn't exist
DB_DIR = Path(__file__).parent / "instance"
DB_DIR.mkdir(exist_ok=True)


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://secureshare_user:postgres@localhost:5432/secureshare_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
