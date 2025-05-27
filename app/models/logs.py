from app.db import db
from datetime import datetime


class Logs(db.Model):
    __tablename__ = 'logs'

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    share_id = db.Column(db.UUID, nullable=False)
    accessed_by = db.Column(db.Integer, nullable=False)
    access_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    ip_address = db.Column(db.String(255), nullable=False)
    user_agent = db.Column(db.String(255), nullable=False)
