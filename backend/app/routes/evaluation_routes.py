from flask import Blueprint, jsonify, request
from app.services.evaluation_service import evaluate_data

bp = Blueprint("evaluation", __name__, url_prefix="/api/evaluation")

@bp.route("/", methods=["POST"])
def evaluate():
    """Evaluate diagnostic data"""
    data = request.get_json()
    result = evaluate_data(data)
    return jsonify(result), 200
