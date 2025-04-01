from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests from browser

# Emission factors
CO2_ELECTRICITY = 0.418
CO2_CAR = 0.332
@app.route('/')
def home():
    return 'Carbon Footprint API is running! please open index.html file '

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        electricity_kwh = float(data.get('electricity', 0))
        car_km = float(data.get('car_km', 0))

        co2_electricity = electricity_kwh * CO2_ELECTRICITY
        co2_car = car_km * CO2_CAR
        total_co2 = co2_electricity + co2_car

        return jsonify({
            "co2_electricity": round(co2_electricity, 2),
            "co2_car": round(co2_car, 2),
            "total_co2": round(total_co2, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
