from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.user.user_service import get_all_users_service, get_user_by_id_service, delete_user_service
from app.user.user_schema import UserSchema

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = get_all_users_service()
    return jsonify(users_schema.dump(users))


@user_bp.route('/user/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = get_user_by_id_service(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))


@user_bp.route('/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()

    if current_user_id != user_id:
        return jsonify({"error": "You can only delete your own account"}), 403

    user = delete_user_service(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))