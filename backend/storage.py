import json
import os
from utils.constants import EMISSION_CATEGORIES

DATA_FILE = "data/reports.json"
stored_reports = []

# Load reports from file on startup
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_reports = json.load(f)

def _save_to_file():
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(stored_reports, f, indent=2)

def save_report(report):
    stored_reports.append(report)
    _save_to_file()

def reset_storage():
    global stored_reports
    stored_reports = []
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def get_all_reports():
    return stored_reports

def get_summary():
    total_users = len(stored_reports)
    if total_users == 0:
        return {
            "total_clients": 0,
            "averages": {key: 0 for key in EMISSION_CATEGORIES}
        }

    summary = {}
    for key in EMISSION_CATEGORIES:
        total = sum(report.get(key, 0) for report in stored_reports)
        summary[key] = round(total / total_users, 2)

    return {
        "total_clients": total_users,
        "averages": summary
    }
