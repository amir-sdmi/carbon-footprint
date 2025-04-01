document.getElementById("carbonForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const electricity = parseFloat(document.getElementById("electricity").value);
  const car_km = parseFloat(document.getElementById("car_km").value);

  fetch("http://127.0.0.1:5000/api/calculate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ electricity, car_km }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.error) throw new Error(data.error);

      document.getElementById("result").style.display = "block";
      document.getElementById("result").innerHTML = `
            <h4>Results</h4>
            <p>Electricity CO₂: ${data.co2_electricity} kg</p>
            <p>Car Travel CO₂: ${data.co2_car} kg</p>
            <strong>Total CO₂: ${data.total_co2} kg</strong>
        `;
    })
    .catch((err) => {
      alert("Error: " + err.message);
    });
});
