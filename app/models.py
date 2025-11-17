from app import db
from datetime import datetime
import uuid


def generate_id():
    return str(uuid.uuid4())


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True, default=generate_id)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    categories = db.relationship('Category', backref='user', lazy=True)
    records = db.relationship('Record', backref='user', lazy=True)


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.String, primary_key=True, default=generate_id)
    name = db.Column(db.String(100), nullable=False)
    is_global = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)

    records = db.relationship('Record', backref='category', lazy=True)


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.String, primary_key=True, default=generate_id)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.String, db.ForeignKey('categories.id'), nullable=True)