from flask import Blueprint, jsonify, request

bp = Blueprint("evaluation", __name__, url_prefix="/api/evaluation")

@bp.route("/", methods=["GET"])
def health():
    return jsonify({"message": "Evaluation route OK"}), 200
