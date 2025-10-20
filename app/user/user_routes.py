from flask import request, jsonify
from app import app
from app.user.user_service import (
    create_user_service,
    get_all_users_service,
    get_user_by_id_service,
    delete_user_service
)

@app.post('/user')
def create_user():
    user_data = request.get_json()
    user = create_user_service(user_data)
    return jsonify(user), 201

@app.get('/users')
def get_users():
    users = get_all_users_service()
    return jsonify(users)

@app.get('/user/<user_id>')
def get_user(user_id):
    user = get_user_by_id_service(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.delete('/user/<user_id>')
def delete_user(user_id):
    result = delete_user_service(user_id)
    if result is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(result)
