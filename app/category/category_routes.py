from flask import Blueprint, request, jsonify
from app.category.category_service import create_category_service, get_all_categories_service, \
    get_user_categories_service, delete_category_service
from app.category.category_schema import CategorySchema

category_bp = Blueprint('category', __name__)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@category_bp.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()

    errors = category_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = create_category_service(data)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(category_schema.dump(result)), 201


@category_bp.route('/category', methods=['GET'])
def get_categories():
    categories = get_all_categories_service()
    return jsonify(categories_schema.dump(categories))


@category_bp.route('/category/user/<user_id>', methods=['GET'])
def get_user_categories(user_id):
    result = get_user_categories_service(user_id)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]
    return jsonify(categories_schema.dump(result))


@category_bp.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    user_id = request.args.get('user_id')
    result = delete_category_service(category_id, user_id)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]
    return jsonify(category_schema.dump(result))