import uuid
from app.storage import categories, records


def generate_id():
    return uuid.uuid4().hex


def create_category_service(category_data):
    category_id = generate_id()
    category = {"id": category_id, **category_data}
    categories[category_id] = category
    return category


def get_all_categories_service():
    return list(categories.values())


def delete_category_service(category_id):
    if category_id not in categories:
        return None

    deleted_category = categories.pop(category_id)

    records_to_delete = [rid for rid, rec in records.items() if rec.get('category_id') == category_id]
    for rid in records_to_delete:
        records.pop(rid)

    return deleted_category
