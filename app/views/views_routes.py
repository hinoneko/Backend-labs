from flask import jsonify
from datetime import datetime
from app import app

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = {
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200
