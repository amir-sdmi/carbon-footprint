# 🌍 Carbon Footprint Calculator

Hey there! This is a simple tool built for the **M602 Computer Programming** course at Gisma University. It helps users calculate their carbon footprint based on things like fuel use, travel, and electricity. You can also see charts and download PDF reports.

---

## ✨ Getting Started

### 1. Clone the Project

First, grab the code from GitHub:

```bash
git clone https://github.com/your-username/carbon-footprint.git
cd carbon-footprint
```

---

### 2. Run the Backend (Python + Flask)

Now let's get the backend running:

```bash
cd backend
python -m venv venv
source venv/bin/activate        # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Your Flask server will start at:

```
http://127.0.0.1:5000
```

Keep this running in the background.

---

### 3. Open the Frontend

In another terminal (or just open a new window):

```bash
cd frontend
```

Now open `index.html` in your browser:

- **Windows**: `start index.html`
- **macOS**: `open index.html`
- **Linux**: `xdg-open index.html`

You can also just double-click the file to open it.

That's it! 🎉 You should now see the app in your browser.

---

## 📊 What This App Can Do

- Simple and clean web interface
- Input travel, fuel, and energy data
- Calculates emissions using EPA data
- Lets you save PDF reports
- Shows pie charts and trends
- Works offline (no install needed!)

---

## 📘 Where We Got Our Data

This project was inspired by:
- [Brightly Software blog](https://www.brightlysoftware.com/blog/calculate-carbon-footprint)
- EPA's Greenhouse Gas Emission Factors Hub (2022)

---

## 📅 Course Details

- **Course**: M602 Computer Programming
- **University**: Gisma University
- **Project Type**: Individual Final Project
- **Due Date**: April 3, 2025

---

## 💼 License

This is an open project under the **MIT License** — feel free to use it, improve it, and make it your own (just give credit!).
