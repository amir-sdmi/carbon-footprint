// Get numeric value from input (float), return 0 if empty or invalid
function getNumber(id) {
  const value = document.getElementById(id).value;
  return value === "" ? 0 : parseFloat(value) || 0;
}
// Get numeric value from input (integer), return 0 if empty or invalid
function getInteger(id) {
  const value = document.getElementById(id).value;
  return value === "" ? 0 : parseInt(value) || 0;
}
// Handle form submission
document.getElementById("carbonForm").addEventListener("submit", function (e) {
  e.preventDefault(); // Stop form from reloading the page

  // Collect input values
  const data = {
    electricity: getNumber("electricity"),
    natural_gas: getNumber("natural_gas"),
    heating_oil: getNumber("heating_oil"),
    car_km: getNumber("car_km"),
    car_fuel_type: document.getElementById("car_fuel_type").value || "gasoline",
    short_flights: getInteger("short_flights"),
    medium_flights: getInteger("medium_flights"),
    long_flights: getInteger("long_flights"),
    waste_kg: getNumber("waste_kg"),
    recycle_plastic: document.getElementById("recycle_plastic").checked,
    recycle_paper: document.getElementById("recycle_paper").checked,
    recycle_glass: document.getElementById("recycle_glass").checked,
    water_liters: getNumber("water_liters"),
  };
  // Send data to backend and handle response
  fetch("http://127.0.0.1:5000/api/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((result) => {
      localStorage.setItem("carbonResult", JSON.stringify(result)); // Store result
      window.location.href = "report.html"; // Go to report page
    })
    .catch((err) => alert("Error: " + err.message)); // Show error if request fails
});
