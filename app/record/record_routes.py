from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.record.record_service import create_record_service, get_record_by_id_service, delete_record_service, \
    get_filtered_records_service
from app.record.record_schema import RecordSchema

record_bp = Blueprint('record', __name__)
record_schema = RecordSchema()
records_schema = RecordSchema(many=True)


@record_bp.route('/record', methods=['POST'])
@jwt_required()
def create_record():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    data['user_id'] = current_user_id

    errors = record_schema.validate(data)
    if errors:
        return jsonify({"errors": errors}), 400

    result = create_record_service(data)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify(record_schema.dump(result)), 201


@record_bp.route('/record/<record_id>', methods=['GET'])
@jwt_required()
def get_record(record_id):
    record = get_record_by_id_service(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404

    current_user_id = get_jwt_identity()
    if record.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    return jsonify(record_schema.dump(record))


@record_bp.route('/record/<record_id>', methods=['DELETE'])
@jwt_required()
def delete_record(record_id):
    current_user_id = get_jwt_identity()

    record = get_record_by_id_service(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404

    if record.user_id != current_user_id:
        return jsonify({"error": "Access denied"}), 403

    deleted_record = delete_record_service(record_id)
    return jsonify(record_schema.dump(deleted_record))


@record_bp.route('/record', methods=['GET'])
@jwt_required()
def get_records():
    current_user_id = get_jwt_identity()
    category_id = request.args.get('category_id')

    records = get_filtered_records_service(current_user_id, category_id)
    return jsonify(records_schema.dump(records))