from app.db import db
from datetime import datetime


class File(db.Model):
    __tablename__ = 'files'

    file_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    original_name = db.Column(db.String(255), nullable=False)
    stored_name = db.Column(db.String(255), nullable=False)
    size_bytes = db.Column(db.Integer, nullable=False)
    mime_type = db.Column(db.String(255), nullable=False)
    encrypted = db.Column(db.Boolean, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f'<File {self.filename}>'


class FileShares(db.Model):
    __tablename__ = 'file_shares'

    share_id = db.Column(db.UUID, primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('files.file_id'), nullable=False)
    shared_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    shared_with = db.Column(db.String(255), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    max_downloads = db.Column(db.Integer, nullable=False)
    password_protected = db.Column(db.Boolean, nullable=False)
    access_password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
