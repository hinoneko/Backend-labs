from app import db
from app.models import Category, User


def create_category_service(data):
    user_id = data.get('user_id')

    if user_id:
        user = User.query.get(user_id)
        if not user:
            return "User not found", 404

    is_global = data.get('is_global', False)
    if is_global:
        user_id = None

    category = Category(
        name=data['name'],
        is_global=is_global,
        user_id=user_id
    )
    db.session.add(category)
    db.session.commit()
    return category


def get_all_categories_service():
    return Category.query.all()


def get_user_categories_service(user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    return Category.query.filter(
        (Category.user_id == user_id)
    ).all()


def delete_category_service(category_id, user_id=None):
    category = Category.query.get(category_id)
    if not category:
        return "Category not found", 404

    if category.user_id and category.user_id != user_id:
        return "Access denied", 403

    db.session.delete(category)
    db.session.commit()
    return category