from app import db
from app.models import User
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token


def register_user_service(data):
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return "Username already exists", 400

    hashed_password = pbkdf2_sha256.hash(data['password'])

    user = User(
        username=data['username'],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return user


def login_user_service(data):
    user = User.query.filter_by(username=data['username']).first()

    if not user or not pbkdf2_sha256.verify(data['password'], user.password):
        return "Invalid username or password", 401

    access_token = create_access_token(identity=user.id)

    return {
        "access_token": access_token,
        "user_id": user.id,
        "username": user.username
    }