from flask import Blueprint, request, jsonify
from app.services.analysis_service import analyze_data

bp = Blueprint("analysis", __name__, url_prefix="/api/analysis")

@bp.route("/", methods=["POST"])
def analyze():
    data = request.get_json()
    result = analyze_data(data)
    return jsonify(result)
