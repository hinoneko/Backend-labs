import uuid
from datetime import datetime
from app.storage import users, categories, records


def generate_id():
    return uuid.uuid4().hex


def get_current_datetime():
    return datetime.now().isoformat()


def create_record_service(record_data):
    record_id = generate_id()

    user_id = record_data.get('user_id')
    category_id = record_data.get('category_id')

    if user_id and user_id not in users:
        return ("User not found", 404)
    if category_id and category_id not in categories:
        return ("Category not found", 404)

    record = {
        "id": record_id,
        "user_id": user_id,
        "category_id": category_id,
        "created_at": get_current_datetime(),
        "amount": record_data.get('amount')
    }
    records[record_id] = record
    return record


def get_record_by_id_service(record_id):
    return records.get(record_id)


def delete_record_service(record_id):
    if record_id not in records:
        return None
    return records.pop(record_id)


def get_filtered_records_service(user_id, category_id):
    if not user_id and not category_id:
        return ("user_id or category_id parameter is required", 400)

    filtered_records = list(records.values())

    if user_id:
        filtered_records = [r for r in filtered_records if r.get('user_id') == user_id]

    if category_id:
        filtered_records = [r for r in filtered_records if r.get('category_id') == category_id]

    return filtered_records
