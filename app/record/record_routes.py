from flask import Blueprint, request, jsonify
from app.record.record_service import create_record_service, get_record_by_id_service, delete_record_service, \
    get_filtered_records_service
from app.record.record_schema import RecordSchema

record_bp = Blueprint('record', __name__)
record_schema = RecordSchema()
records_schema = RecordSchema(many=True)


@record_bp.route('/record', methods=['POST'])
def create_record():
    data = request.get_json()

    errors = record_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = create_record_service(data)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(record_schema.dump(result)), 201


@record_bp.route('/record/<record_id>', methods=['GET'])
def get_record(record_id):
    record = get_record_by_id_service(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record_schema.dump(record))


@record_bp.route('/record/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = delete_record_service(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404
    return jsonify(record_schema.dump(record))


@record_bp.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    records = get_filtered_records_service(user_id, category_id)
    return jsonify(records_schema.dump(records))