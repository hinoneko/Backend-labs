import uuid
from app.storage import (users, records)


def generate_id():
    return uuid.uuid4().hex


def create_user_service(user_data):
    user_id = generate_id()
    user = {"id": user_id, **user_data}
    users[user_id] = user
    return user


def get_all_users_service():
    return list(users.values())


def get_user_by_id_service(user_id):
    return users.get(user_id)


def delete_user_service(user_id):
    if user_id not in users:
        return None

    deleted_user = users.pop(user_id)

    records_to_delete = [rid for rid, rec in records.items() if rec.get('user_id') == user_id]
    for rid in records_to_delete:
        records.pop(rid)

    return deleted_user
