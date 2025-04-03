from flask import Blueprint, request, jsonify, send_from_directory
from services.calculator import calculate_emissions
from storage import get_summary, reset_storage
import shutil

calculate_bp = Blueprint('calculate', __name__, url_prefix='/api')

# Reset all stored data and delete reports
@calculate_bp.route('/reset', methods=['POST'])
def reset():
    reset_storage()
    shutil.rmtree("reports", ignore_errors=True)
    return jsonify({"message": "All data and reports cleared."})

# Calculate carbon footprint based on user input
@calculate_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        result = calculate_emissions(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get emissions summary
@calculate_bp.route('/summary', methods=['GET'])
def summary():
    return jsonify(get_summary())

# Download generated PDF report
@calculate_bp.route('/reports/<filename>', methods=['GET'])
def download_report(filename):
    return send_from_directory("reports", filename)
