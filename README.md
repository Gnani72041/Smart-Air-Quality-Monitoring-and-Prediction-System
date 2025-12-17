# 🌍 Smart Air Quality Monitoring and Prediction System

## 📌 Project Overview

The **Smart Air Quality Monitoring and Prediction System** is an end-to-end IoT and Machine Learning–based solution designed to **monitor, analyze, and predict air quality in real time**. The system integrates environmental sensors with a cloud platform and a trained ML model to calculate the **Air Quality Index (AQI)**, classify pollution levels, and provide **actionable health recommendations and alerts**.

This project is developed as a **final-year capstone project**, following industry-level architecture and best practices, and is suitable for real-world deployment scenarios such as smart cities, residential monitoring, and public health systems.

---

## 🎯 Objectives

* To collect real-time environmental data using IoT sensors
* To preprocess and structure air quality data for ML analysis
* To predict AQI using machine learning models
* To classify air quality into standard AQI categories
* To generate health recommendations based on AQI levels
* To notify users via alerts when air quality becomes unhealthy
* To provide a professional web-based dashboard for interaction

---

## 🧠 Key Features

* ✅ Real-time air quality monitoring using IoT
* ✅ Machine Learning–based AQI prediction
* ✅ AQI category classification (Good, Moderate, Poor, etc.)
* ✅ Health risk analysis & recommendations
* ✅ Interactive Flask-based web application
* ✅ Data visualization using charts and AQI gauge
* ✅ Scalable cloud integration (ThingSpeak + Blynk)
* ✅ Alert system (Email/SMS-ready architecture)

---

## 🏗️ System Architecture

**Data Flow:**

```
Sensors → NodeMCU → ThingSpeak → Flask Backend → ML Models → Web Dashboard & Alerts
```

### Components:

* **IoT Layer:** NodeMCU (ESP8266/ESP32), MQ-135, DHT11
* **Cloud Layer:** ThingSpeak (data ingestion), Blynk (optional dashboard)
* **ML Layer:** Random Forest Regressor & Classifier
* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript, Chart.js
* **Deployment:** Localhost / Cloud-ready

---

## 📊 Dataset Description

The dataset is sourced from **Kaggle** and CPCB-aligned air quality records.

### Input Features:

| Feature | Description                       | Unit  |
| ------- | --------------------------------- | ----- |
| PM2.5   | Fine particulate matter (<2.5µm)  | µg/m³ |
| PM10    | Coarse particulate matter (<10µm) | µg/m³ |
| NO₂     | Nitrogen Dioxide                  | µg/m³ |
| SO₂     | Sulphur Dioxide                   | µg/m³ |
| CO      | Carbon Monoxide                   | mg/m³ |
| O₃      | Ozone                             | µg/m³ |

### Target Variables:

* **AQI (Continuous value)** – Regression output
* **AQI Category** – Classification output

---

## 🧮 AQI Calculation & Categories

AQI is predicted using ML rather than manual formula calculation to:

* Handle **non-linear relationships** between pollutants
* Be **robust to outliers and noise**
* Improve accuracy over rule-based systems

### AQI Categories:

| AQI Range | Category     | Health Impact             |
| --------- | ------------ | ------------------------- |
| 0–50      | Good         | Minimal impact            |
| 51–100    | Satisfactory | Minor discomfort          |
| 101–200   | Moderate     | Sensitive groups affected |
| 201–300   | Poor         | Breathing discomfort      |
| 301–400   | Very Poor    | Health effects likely     |
| 401–500   | Severe       | Serious health risk       |

---

## 🤖 Machine Learning Models Used

### Regression (AQI Prediction):

* Random Forest Regressor ⭐ (Best)
* Extra Trees Regressor
* Gradient Boosting Regressor

### Classification (AQI Category):

* Random Forest Classifier ⭐ (Best)
* Logistic Regression
* XGBoost Classifier

**Why Random Forest?**

* Captures complex non-linear patterns
* Handles multicollinearity
* Resistant to outliers
* High accuracy and generalization

---

## 🌐 Web Application Workflow

1. User enters pollutant values via UI
2. Flask backend receives data
3. Input is scaled using saved scalers
4. ML models predict AQI and category
5. Health recommendations are generated
6. Results are visualized with charts
7. Alerts are triggered if AQI exceeds threshold

---

## 🚨 Alert System

* Triggered when AQI crosses unsafe limits
* Sends alerts with:

  * AQI value
  * Pollution category
  * Health recommendations
* Extendable to Email, SMS, or Push Notifications

---

## 🛠️ Tech Stack

* **Programming:** Python
* **ML Libraries:** Scikit-learn, Pandas, NumPy
* **Web:** Flask, HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **IoT:** NodeMCU, MQ-135, DHT11
* **Cloud:** ThingSpeak, Blynk
* **Model Storage:** Joblib

---

## 📂 Project Structure

```
Smart-Air-Quality-Monitoring/
│
├── app.py
├── model/
│   ├── predict.py
│   ├── best_regression_model.pkl
│   ├── best_classification_model.pkl
│   ├── scaler_regression.pkl
│   ├── scaler_classification.pkl
│   └── label_encoder.pkl
├── templates/
│   ├── index.html
│   └── result.html
├── dataset/
│   └── air_quality_with_dominant_healthrisk.csv
├── README.md
└── requirements.txt
```

---

## 🚀 Future Enhancements

* Real-time IoT data integration (live sensors)
* LSTM-based time-series prediction
* Mobile app integration
* GIS-based pollution mapping
* Government dashboard integration (CPCB/EPA)

---

## 👨‍💻 Author

**Gnanesh M**
Final Year B.Tech – Computer Science & Engineering

🔗 LinkedIn: [https://www.linkedin.com/in/gnanesh-m-a13960301](https://www.linkedin.com/in/gnanesh-m-a13960301)

---

## ⭐ Recruiter Note

This project demonstrates:

* End-to-end ML system design
* IoT + Cloud + ML integration
* Practical problem-solving
* Industry-relevant architecture

If you like this project, ⭐ the repository!
