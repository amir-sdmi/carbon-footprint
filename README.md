# 🌍 Carbon Footprint Calculator

This project is developed as part of the **M602 Computer Programming** course at Gisma University. It is a web-based application that allows users to input activity data (fuel, travel, electricity usage, etc.) and calculates the resulting carbon emissions. The tool also generates visual summaries and downloadable PDF reports.

---

## 📁 Project Structure

```
carbon-footprint/
├── backend/          # Python Flask backend server
│   ├── app.py        # Main Flask app
│   ├── data/         # Stores report data in JSON format
│   ├── reports/      # Folder where generated PDF reports are saved
│   └── requirements.txt
├── frontend/         # Frontend with HTML, CSS, and JavaScript
│   └── index.html    # Main UI
└── README.md         # You're here!
```

---

## ✨ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/carbon-footprint.git
cd carbon-footprint
```

---

### 2. Backend Setup (Python + Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The Flask backend will start running at:

```
http://127.0.0.1:5000
```

Keep it running while using the frontend.

---

### 3. Frontend Setup

In a **new terminal window**:

```bash
cd frontend
```

Now open the app:

- **Windows**: `start index.html`
- **macOS**: `open index.html`
- **Linux**: `xdg-open index.html`

Or simply double-click `index.html` in your file explorer.

That's it! 🎉 Enjoy using the Carbon Footprint Calculator.

---

## 📊 Features

- Easy-to-use web interface
- Input for travel, fuel, and electricity usage
- Emission calculations using official EPA factors
- PDF report generation
- Visual charts and summaries
- Offline-ready frontend (no build tools required)

---

## 📘 Reference

Emission factors and methodology are inspired by:
- Brightly Software: [How to calculate your carbon footprint](https://www.brightlysoftware.com/blog/calculate-carbon-footprint)
- U.S. EPA: Greenhouse Gas Emission Factors Hub (April 2022)

---

## 📅 Course Info

- **Module**: M602 Computer Programming
- **University**: Gisma University of Applied Sciences
- **Assessment**: Final Individual Project
- **Deadline**: April 3, 2025

---

## 📊 License

This project is licensed under the **MIT License**. You are free to use and modify it with proper attribution.

