from app.db import db
from datetime import datetime


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    file_path = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f'<File {self.filename}>'
