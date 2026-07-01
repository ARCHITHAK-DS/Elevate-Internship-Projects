<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=Data%20Science%20Portfolio&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Customer%20LTV%20Prediction%20%C2%B7%20EV%20Charging%20Demand%20Forecasting&descAlignY=58&descAlign=50" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-ML%20Model-FF6600?style=for-the-badge&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-0668E1?style=for-the-badge&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)

<br/>

### 👤 Architha K &nbsp;·&nbsp; Data Science Portfolio &nbsp;·&nbsp; 2024

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)

<br/>

> *"Two projects. Two domains. One goal — turn raw data into decisions."*

</div>

---

<br/>

## 📂 Portfolio Overview

This repository contains **two end-to-end Data Science projects** covering different ML paradigms, business domains, and tool stacks — demonstrating range across regression, time-series forecasting, anomaly detection, dashboarding, and web app deployment.

<div align="center">

| | Project 1 | Project 2 |
|:---:|:---:|:---:|
| **Name** | Customer LTV Prediction | EV Charging Demand Forecasting |
| **Domain** | E-commerce / Marketing | Energy / Infrastructure |
| **ML Type** | Regression | Time-Series Forecasting |
| **Core Model** | XGBoost | ARIMA + Prophet |
| **App** | Streamlit (Live) | Tableau Dashboard |
| **Bonus** | SHAP · Churn Layer | Anomaly Detection · Optimizer |

</div>

<br/>

---

<br/>

# 🛒 Project 1 — Customer Lifetime Value Prediction

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![XGBoost](https://img.shields.io/badge/-XGBoost-FF6600?style=flat-square)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square)
![Excel](https://img.shields.io/badge/-Excel-217346?logo=microsoft-excel&logoColor=white&style=flat-square)

**[🌐 Live Demo](https://your-ltv-app.streamlit.app)** &nbsp;·&nbsp; **[📓 Notebook](./Customer_LTV_Prediction.ipynb)** &nbsp;·&nbsp; **[📊 Report](./LTV_Project_Report.pdf)**

</div>

### 🧠 What it does

Predicts how much each customer will spend in the next 6 months — before they spend it — using RFM feature engineering and XGBoost regression. Segments customers into 4 marketing tiers.

### 📊 Results

```
MAE   : ₹124.50   |   RMSE : ₹298.70   |   R² : 0.847   |   Accuracy: 81.2%
```

### ✨ Customer Segments

```
⭐ VIP     │ Avg LTV: ₹2,350 │ Top 12.5% │ → Loyalty rewards & early access
🔵 HIGH    │ Avg LTV: ₹890   │ Top 25%   │ → Upsell premium bundles
🔷 MEDIUM  │ Avg LTV: ₹380   │ Top 50%   │ → Personalised re-engagement
⚪ LOW     │ Avg LTV: ₹75    │ Bottom    │ → Low-cost retention only
```

### 🗂️ Files

```
📦 Project 1/
├── 📓 Customer_LTV_Prediction.ipynb   ← Full 10-step ML notebook
├── 🌐 app.py                          ← Streamlit Glassmorphism web app
├── 📊 LTV_Excel_Report.xlsx           ← 4-sheet Excel business report
├── 📽️  LTV_Presentation.pptx          ← 8-slide portfolio deck
├── 📄 LTV_Project_Report.pdf          ← 2-page project report
└── 🤖 ltv_model.pkl                   ← Trained XGBoost model
```

### ⚙️ Feature Importance

```
Monetary      ██████████████████████████████████  34.2%
Recency       ████████████████████████            22.8%
Frequency     ███████████████████                 18.7%
Tenure        ████████████                        11.2%
AOV           █████████                            8.1%
Unique Prods  ██████                               5.0%
```

### 🚀 Run Locally

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit joblib openpyxl
# Download OnlineRetail.xlsx from Kaggle → place in folder
jupyter notebook Customer_LTV_Prediction.ipynb
streamlit run app.py
```

<br/>

---

<br/>

# ⚡ Project 2 — EV Charging Demand Forecasting

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![Prophet](https://img.shields.io/badge/-Prophet-0668E1?style=flat-square)
![ARIMA](https://img.shields.io/badge/-ARIMA-7B61FF?style=flat-square)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?logo=tableau&logoColor=white&style=flat-square)

**[📊 Tableau Dashboard](#)** &nbsp;·&nbsp; **[📓 Notebook](./EV_Charging_Notebook.ipynb)** &nbsp;·&nbsp; **[📄 Report](./EV_Project_Report.pdf)**

</div>

### 🧠 What it does

Forecasts hourly demand at EV charging stations 30 days ahead using ARIMA and Prophet, with weather feature integration. Includes anomaly detection and a charging optimization engine.

### 📊 Results

```
ARIMA   → MAE: 0.412  |  RMSE: 0.587  |  Seasonality: Manual
Prophet → MAE: 0.298  |  RMSE: 0.431  |  Seasonality: Auto ✅  ← Winner
```

### 🗺️ Dataset Coverage

```
📍 5 Stations  ·  2 Cities (Bangalore + Chennai)
📅 1 Year      ·  Hourly resolution  ·  43,800 records
🌡️  Weather    ·  Temperature · Rainfall · Wind speed
⚡ Demand      ·  Units charged · Utilisation % · Anomaly flag
```

### 🚀 BONUS Features

```
🔴 Anomaly Detection   → Z-score (threshold > 3.0) flags unusual demand spikes
                         Evaluated with precision-recall classification report

⚡ Optimization Engine → Recommends top 5 station-hour slots by availability
                         Input: city, date, preferred hours
                         Output: ranked charging windows with ⭐ Best Slot label
```

### 🗂️ Files

```
📦 Project 2/
├── 📓 EV_Charging_Notebook.ipynb      ← Full 10-step forecasting notebook
├── 📊 EV_Charging_Demand.csv          ← Raw dataset (43,800 rows)
├── 📊 EV_Tableau_Ready.csv            ← Aggregated CSV for Tableau
├── 📊 EV_Anomaly_Report.csv           ← Detected anomalies export
├── 📊 EV_Optimization_Strategy.csv    ← Best charging slots per city
├── 📈 EV_Excel_Report.xlsx            ← Station performance report
└── 📄 EV_Project_Report.pdf           ← 2-page project report
```

### 🗒️ Tableau Setup (Quick Guide)

```
1. Open Tableau Public (free) → Connect → Text File → EV_Tableau_Ready.csv
2. Drag 'hour' to Columns, 'day_name' to Rows, 'avg_demand' to Color
   → You get the demand heatmap
3. Drag 'month_name' to Columns, 'avg_demand' to Rows
   → Monthly demand trend line chart
4. Filter by 'city' or 'station_name' for station-level drill-down
5. Publish to Tableau Public → copy the share link
```

### 🚀 Run Locally

```bash
pip install pandas numpy matplotlib seaborn statsmodels prophet scikit-learn openpyxl
jupyter notebook EV_Charging_Notebook.ipynb
```

<br/>

---

<br/>

## 🧰 Combined Tech Stack

<div align="center">

| Layer | Project 1 (LTV) | Project 2 (EV) |
|:---:|:---:|:---:|
| Language | Python 3.9+ | Python 3.9+ |
| ML / Model | XGBoost, Random Forest | ARIMA, Prophet |
| Features | RFM Engineering | Weather + Temporal |
| Bonus | Segmentation + Glassmorphism App | Anomaly Detection + Optimizer |
| Dashboard | Streamlit (live) | Tableau Public |
| Report | Excel 4-sheet + PPTX | Excel + CSV exports |
| Validation | MAE, RMSE, R² | MAE, RMSE, Precision-Recall |

</div>

<br/>

---

## 🗺️ Repository Structure

```
📦 data-science-portfolio/
│
├── 📁 project-1-ltv/
│   ├── Customer_LTV_Prediction.ipynb
│   ├── app.py
│   ├── LTV_Excel_Report.xlsx
│   ├── LTV_Presentation.pptx
│   ├── LTV_Project_Report.pdf
│   └── requirements_ltv.txt
│
├── 📁 project-2-ev/
│   ├── EV_Charging_Notebook.ipynb
│   ├── EV_Charging_Demand.csv
│   ├── EV_Tableau_Ready.csv
│   ├── EV_Anomaly_Report.csv
│   ├── EV_Optimization_Strategy.csv
│   ├── EV_Excel_Report.xlsx
│   ├── EV_Project_Report.pdf
│   └── requirements_ev.txt
│
└── 📄 README.md   ← You are here
```

<br/>

---

## 🗺️ Roadmap

- [x] LTV Prediction — XGBoost + RFM
- [x] LTV Streamlit App — Glassmorphism UI
- [x] LTV Excel 4-sheet Report
- [x] LTV 8-slide PPTX Presentation
- [x] EV Demand Forecasting — ARIMA + Prophet
- [x] EV Anomaly Detection — Z-score
- [x] EV Charging Optimization Engine
- [x] EV Tableau-ready CSV export
- [ ] SHAP explainability for LTV model
- [ ] BG/NBD probabilistic CLV model
- [ ] Live weather API integration for EV forecasting
- [ ] Combined Streamlit multi-project portfolio app

<br/>

---

<div align="center">

**If this helped you, please ⭐ star the repo!**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Architha%20K-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer&animation=fadeIn" width="100%"/>
