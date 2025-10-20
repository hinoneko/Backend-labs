from flask import request, jsonify
from app import app
from app.category.category_service import (
    create_category_service,
    get_all_categories_service,
    delete_category_service
)

@app.post('/category')
def create_category():
    category_data = request.get_json()
    category = create_category_service(category_data)
    return jsonify(category), 201

@app.get('/category')
def get_categories():
    categories = get_all_categories_service()
    return jsonify(categories)

@app.delete('/category/<category_id>')
def delete_category(category_id):
    result = delete_category_service(category_id)
    if result is None:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(result)
