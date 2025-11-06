from flask import Blueprint, jsonify, request
from app.services.recommendation_service import generate_recommendations

bp = Blueprint("recommendation", __name__, url_prefix="/api/recommendation")

@bp.route("/", methods=["POST"])
def recommend():
    """Generate recommendations based on evaluation"""
    data = request.get_json()
    result = generate_recommendations(data)
    return jsonify(result), 200
