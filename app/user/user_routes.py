from flask import Blueprint, request, jsonify
from app.user.user_service import create_user_service, get_all_users_service, get_user_by_id_service, \
    delete_user_service
from app.user.user_schema import UserSchema

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    errors = user_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = create_user_service(data)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(user_schema.dump(result)), 201


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users_service()
    return jsonify(users_schema.dump(users))


@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id_service(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))


@user_bp.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = delete_user_service(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))