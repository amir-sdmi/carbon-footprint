from flask import Blueprint, request, jsonify
from services.calculator import calculate_emissions
from storage import get_summary,reset_storage
import shutil

calculate_bp = Blueprint('calculate', __name__, url_prefix='/api')


@calculate_bp.route('/reset', methods=['POST'])
def reset():
    reset_storage()
    shutil.rmtree("reports", ignore_errors=True)
    return jsonify({"message": "All data and reports cleared."})

@calculate_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        result = calculate_emissions(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@calculate_bp.route('/summary', methods=['GET'])
def summary():
    return jsonify(get_summary())