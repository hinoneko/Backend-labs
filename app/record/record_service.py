from app import db
from app.models import Record, User, Category


def create_record_service(data):
    user = User.query.get(data['user_id'])
    if not user:
        return "User not found", 404

    category_id = data.get('category_id')
    if category_id:
        category = Category.query.get(category_id)
        if not category:
            return "Category not found", 404

        if category.user_id and category.user_id != data['user_id']:
            return "Cannot use this category", 403

    record = Record(
        amount=data['amount'],
        user_id=data['user_id'],
        category_id=category_id
    )
    db.session.add(record)
    db.session.commit()
    return record


def get_record_by_id_service(record_id):
    return Record.query.get(record_id)


def delete_record_service(record_id):
    record = Record.query.get(record_id)
    if not record:
        return None
    db.session.delete(record)
    db.session.commit()
    return record


def get_filtered_records_service(user_id=None, category_id=None):
    query = Record.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    if category_id:
        query = query.filter_by(category_id=category_id)
    return query.all()