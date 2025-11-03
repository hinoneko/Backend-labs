from flask import jsonify, Blueprint
from datetime import datetime

views_bp = Blueprint('views', __name__)

@views_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = {
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200
