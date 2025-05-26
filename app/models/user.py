from datetime import datetime

from app.db import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Serial, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128))
    mfa_enabled = db.Column(db.Boolean, default=False)
    mfa_secret = db.Column(db.String(128))
    role = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
