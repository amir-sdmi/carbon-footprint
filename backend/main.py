def calculate_electricity_emissions(kwh):
    # Emission factor: 0.418 kg CO2 per kWh
    return kwh * 0.418

def calculate_car_emissions(km):
    # Emission factor: 0.332 kg CO2 per km (approx, from EPA data)
    return km * 0.332

def main():
    print("Welcome to the Carbon Footprint Calculator")

    try:
        electricity_kwh = float(input("Enter your monthly electricity usage in kWh: "))
        car_km = float(input("Enter kilometers you drive per month: "))

        co2_from_electricity = calculate_electricity_emissions(electricity_kwh)
        co2_from_car = calculate_car_emissions(car_km)
        total_co2 = co2_from_electricity + co2_from_car

        print("\n--- Carbon Footprint Report ---")
        print(f"Electricity CO2: {co2_from_electricity:.2f} kg")
        print(f"Car Travel CO2: {co2_from_car:.2f} kg")
        print(f"Total Monthly CO2 Emissions: {total_co2:.2f} kg")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
