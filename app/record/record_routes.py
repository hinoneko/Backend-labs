from flask import request, jsonify
from app import app
from app.record.record_service import (
    create_record_service,
    get_record_by_id_service,
    delete_record_service,
    get_filtered_records_service
)


@app.post('/record')
def create_record():
    record_data = request.get_json()
    result = create_record_service(record_data)

    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(result), 201


@app.get('/record/<record_id>')
def get_record(record_id):
    record = get_record_by_id_service(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record)


@app.delete('/record/<record_id>')
def delete_record(record_id):
    result = delete_record_service(record_id)
    if result is None:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(result)


@app.get('/record')
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    result = get_filtered_records_service(user_id, category_id)

    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(result)
