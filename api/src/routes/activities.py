from flask import Blueprint, jsonify

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"})