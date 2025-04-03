from utils.constants import FACTORS, EMISSION_CATEGORIES
from storage import save_report, get_summary
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import uuid

# Main function to calculate emissions based on user input
def calculate_emissions(data):
    # Extract and convert user input
    electricity = float(data.get("electricity", 0))
    natural_gas = float(data.get("natural_gas", 0))
    heating_oil = float(data.get("heating_oil", 0))
    car_km = float(data.get("car_km", 0))
    fuel_type = data.get("car_fuel_type", "gasoline")
    fuel_key = "electric_car" if fuel_type == "electric" else fuel_type
    short_flights = int(data.get("short_flights", 0))
    medium_flights = int(data.get("medium_flights", 0))
    long_flights = int(data.get("long_flights", 0))
    waste_kg = float(data.get("waste_kg", 0))
    recycle_plastic = data.get("recycle_plastic", False)
    recycle_paper = data.get("recycle_paper", False)
    recycle_glass = data.get("recycle_glass", False)
    water_liters = float(data.get("water_liters", 0))
    # Calculate emissions for each category
    co2_electricity = electricity * FACTORS["electricity"]
    co2_natural_gas = natural_gas * FACTORS["natural_gas"]
    co2_heating_oil = heating_oil * FACTORS["heating_oil"]
    co2_car = car_km * FACTORS.get(fuel_key, 0.332)
    co2_flights = (
        short_flights * FACTORS["flight_short"] +
        medium_flights * FACTORS["flight_medium"] +
        long_flights * FACTORS["flight_long"]
    )
    co2_waste = waste_kg * FACTORS["waste"]
    co2_water = water_liters * FACTORS["water"]
    # Calculate emission savings from recycling
    co2_recycling_saved = 0
    if recycle_plastic:
        co2_recycling_saved += FACTORS["recycling_saving"]["plastic"]
    if recycle_paper:
        co2_recycling_saved += FACTORS["recycling_saving"]["paper"]
    if recycle_glass:
        co2_recycling_saved += FACTORS["recycling_saving"]["glass"]
    # Final total CO₂e value
    total_co2e = (
        co2_electricity + co2_natural_gas + co2_heating_oil +
        co2_car + co2_flights + co2_waste + co2_water -
        co2_recycling_saved
    )
    # Prepare result data
    result = {
        "co2_electricity": round(co2_electricity, 2),
        "co2_natural_gas": round(co2_natural_gas, 2),
        "co2_heating_oil": round(co2_heating_oil, 2),
        "co2_car": round(co2_car, 2),
        "co2_flights": round(co2_flights, 2),
        "co2_waste": round(co2_waste, 2),
        "co2_water": round(co2_water, 2),
        "co2_recycling_saved": round(co2_recycling_saved, 2),
        "total_co2e": round(total_co2e, 2)
    }
    # Add chart data for frontend use
    result["chart_data"] = {
        "pie": {
            "Electricity": co2_electricity,
            "Natural Gas": co2_natural_gas,
            "Heating Oil": co2_heating_oil,
            "Car": co2_car,
            "Flights": co2_flights,
            "Waste": co2_waste,
            "Water": co2_water,
            "Recycling Savings": -co2_recycling_saved
        },
        "trend": {
            "user_total": round(total_co2e, 2),
            "average_total": get_summary()["averages"].get("total_co2e", 0)
        }
    }
    # Generate PDF report and save result
    result["pdf_filename"] = generate_pdf(result)
    save_report(result)
    return result

# Generate a PDF report based on emission results
def generate_pdf(report_data):
    os.makedirs("reports", exist_ok=True)
    filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
    filepath = os.path.join("reports", filename)

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors

    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Report title
    elements.append(Paragraph("Carbon Footprint Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # User's personal emissions
    elements.append(Paragraph("👤 Your Monthly Footprint", styles["Heading2"]))
    user_table = [["Category", "Emissions (kg CO2)"]]
    for key in EMISSION_CATEGORIES:
        label = key.replace("co2_", "").replace("_", " ").title()
        value = report_data.get(key, 0)
        user_table.append([label, f"{value}"])

    user_table_style = Table(user_table)
    user_table_style.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(user_table_style)
    elements.append(Spacer(1, 20))

    # Summary of average emissions
    summary = get_summary()
    elements.append(Paragraph(
        f"📈 Summary Trends Across {summary['total_clients']} Client{'s' if summary['total_clients'] != 1 else ''}",
        styles["Heading2"]
    ))
    summary_table = [["Category", "Average (kg CO2e)"]]
    for key in EMISSION_CATEGORIES:
        label = key.replace("co2_", "").replace("_", " ").title()
        avg_value = summary["averages"].get(key, 0)
        summary_table.append([label, f"{avg_value}"])

    summary_table_style = Table(summary_table)
    summary_table_style.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(summary_table_style)

    # Save the PDF
    doc.build(elements)
    return filename
