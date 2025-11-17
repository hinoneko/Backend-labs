from flask import Blueprint, request, jsonify
from app.auth.auth_service import register_user_service, login_user_service
from app.auth.auth_schema import RegisterSchema, LoginSchema

auth_bp = Blueprint('auth', __name__)
register_schema = RegisterSchema()
login_schema = LoginSchema()


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    errors = register_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = register_user_service(data)

    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify({
        "message": "User registered successfully",
        "user_id": result.id,
        "username": result.username
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    errors = login_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = login_user_service(data)

    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(result), 200