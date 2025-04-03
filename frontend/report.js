// Keys used for emissions categories
const EMISSION_KEYS = [
  "co2_electricity",
  "co2_natural_gas",
  "co2_heating_oil",
  "co2_car",
  "co2_flights",
  "co2_waste",
  "co2_water",
  "co2_recycling_saved",
  "total_co2e",
];

// When page loads, get stored result and display it
window.onload = () => {
  const result = JSON.parse(localStorage.getItem("carbonResult"));
  if (!result) {
    document.getElementById("resultTable").innerHTML =
      "<p>No report available. Please go back and submit the form.</p>";
    return;
  }

  // Create table rows from result data
  const resRows = EMISSION_KEYS.map((key) => {
    const label = key.replace(/_/g, " ").replace("co2 ", "").toUpperCase();
    return `<tr><td>${label}</td><td>${result[key]} kg</td></tr>`;
  }).join("");

  // Render user result table
  document.getElementById("resultTable").innerHTML = `
      <thead><tr><th>Category</th><th>Emissions</th></tr></thead>
      <tbody>${resRows}</tbody>
    `;

  // Set PDF download link
  document.getElementById(
    "downloadLink"
  ).href = `http://127.0.0.1:5000/api/reports/${result.pdf_filename}`;

  // Show charts and summary
  renderPieChart(result.chart_data.pie);
  renderTrendChart(result.chart_data.trend);
  loadSummary();
};

// Render pie chart of emission breakdown
function renderPieChart(pieData) {
  new Chart(document.getElementById("pieChart"), {
    type: "pie",
    data: {
      labels: Object.keys(pieData),
      datasets: [
        {
          data: Object.values(pieData),
          backgroundColor: [
            "#3498db",
            "#e67e22",
            "#f39c12",
            "#2ecc71",
            "#9b59b6",
            "#e74c3c",
            "#1abc9c",
            "#7f8c8d",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
          labels: { font: { size: 12 }, color: "#2c3e50" },
        },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.label}: ${ctx.formattedValue} kg`,
          },
        },
        title: {
          display: true,
          text: "Your CO₂ Emissions Breakdown",
          font: { size: 16 },
          color: "#34495e",
        },
      },
    },
  });
}

// Render bar chart comparing user vs average
function renderTrendChart(trendData) {
  new Chart(document.getElementById("trendChart"), {
    type: "bar",
    data: {
      labels: ["You", "Average (All Users)"],
      datasets: [
        {
          label: "Total Emissions (kg CO₂e)",
          data: [trendData.user_total, trendData.average_total],
          backgroundColor: ["#2980b9", "#95a5a6"],
          borderRadius: 6,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: ${ctx.formattedValue} kg`,
          },
        },
        title: {
          display: true,
          text: "You vs Average User",
          font: { size: 16 },
          color: "#34495e",
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: { color: "#2c3e50", font: { size: 12 } },
          title: {
            display: true,
            text: "kg CO₂e",
            color: "#7f8c8d",
            font: { size: 12 },
          },
        },
        x: {
          ticks: { color: "#2c3e50", font: { size: 12 } },
        },
      },
    },
  });
}

// Load average summary data from backend
function loadSummary() {
  fetch("http://127.0.0.1:5000/api/summary")
    .then((res) => res.json())
    .then((summary) => {
      if (summary.total_clients === 0) {
        document.getElementById("summaryTable").innerHTML =
          "<p>No data available.</p>";
        return;
      }

      const summaryRows = EMISSION_KEYS.map((key) => {
        const label = key.replace(/_/g, " ").replace("co2 ", "").toUpperCase();
        const value = summary.averages[key] || 0;
        return `<tr><td>${label}</td><td>${value} kg</td></tr>`;
      }).join("");

      // Update heading with total clients
      const header = document.querySelector(".summary-section h4");
      header.textContent = `📈 Summary Trends (Across ${
        summary.total_clients
      } Client${summary.total_clients !== 1 ? "s" : ""})`;

      // Render summary table
      document.getElementById("summaryTable").innerHTML = `
        <thead><tr><th>Category</th><th>Average</th></tr></thead>
        <tbody>${summaryRows}</tbody>
      `;
    });
}

// Reset all stored data
function resetAll() {
  fetch("http://127.0.0.1:5000/api/reset", { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      alert(data.message);
      localStorage.removeItem("carbonResult");
      window.location.href = "index.html";
    })
    .catch((err) => alert("Reset failed: " + err.message));
}

// Start a new calculation
function startNew() {
  localStorage.removeItem("carbonResult");
  window.location.href = "index.html";
}
