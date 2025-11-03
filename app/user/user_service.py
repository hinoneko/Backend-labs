from app import db
from app.models import User


def create_user_service(data):
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return "Username already exists", 400

    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()
    return user


def get_all_users_service():
    return User.query.all()


def get_user_by_id_service(user_id):
    return User.query.get(user_id)


def delete_user_service(user_id):
    user = User.query.get(user_id)
    if not user:
        return None

    db.session.delete(user)
    db.session.commit()
    return user