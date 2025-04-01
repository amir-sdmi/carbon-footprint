FACTORS = {
    "electricity": 0.418,            # kg CO2 per kWh
    "natural_gas": 0.05444,          # kg CO2 per cubic foot
    "heating_oil": 10.21,            # kg CO2 per gallon

    "gasoline": 0.332,               # kg CO2 per km
    "diesel": 0.38,
    "electric_car": 0.1,

    "flight_short": 110,
    "flight_medium": 250,
    "flight_long": 400,

    "waste": 0.57,
    "water": 0.0003,

    "recycling_saving": {
        "plastic": 1.5,
        "paper": 1.0,
        "glass": 0.5
    }
}

EMISSION_CATEGORIES = [
    "co2_electricity",
    "co2_natural_gas",
    "co2_heating_oil",
    "co2_car",
    "co2_flights",
    "co2_waste",
    "co2_water",
    "co2_recycling_saved",
    "total_co2e"
]
