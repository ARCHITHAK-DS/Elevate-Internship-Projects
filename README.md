<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=240&section=header&text=Data%20Science%20Portfolio&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Architha%20K%20%20%C2%B7%20%20Python%20%C2%B7%20Machine%20Learning%20%C2%B7%20Forecasting%20%C2%B7%20Tableau&descAlignY=56&descAlign=50&descSize=13" width="100%"/>

</div>

<br/>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/Architha%20K-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
&nbsp;
[![Tableau](https://img.shields.io/badge/Tableau-Live%20Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1)
&nbsp;
[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-ltv-app.streamlit.app)

</div>

<br/>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   Two projects. Two domains. One mission.                            ║
║   Turn raw data into decisions that actually matter.                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

---

<br/>

## 🗂 What's Inside

<div align="center">

|  | 🛒 Project 1 | ⚡ Project 2 |
|:---:|:---:|:---:|
| **Name** | Customer LTV Prediction | EV Charging Demand Forecasting |
| **Domain** | E-commerce · Marketing | Energy · Infrastructure |
| **Core Question** | *Who will spend the most — and how much?* | *When will stations be overcrowded — and where?* |
| **ML Type** | Supervised Regression | Time-Series Forecasting |
| **Model** | XGBoost · Random Forest | ARIMA · Facebook Prophet |
| **Bonus** | 4-tier Segmentation · Glassmorphism App | Anomaly Detection · Optimizer Engine |
| **Dashboard** | Streamlit (Live 🟢) | Tableau Public (Live 🟢) |
| **Accuracy** | R² = 0.847 · MAE ₹124 | Prophet RMSE 26% < ARIMA |

</div>

<br/>

---

<br/>

<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PROJECT  1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

# 🛒 Customer Lifetime Value Prediction

</div>

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![XGBoost](https://img.shields.io/badge/-XGBoost-FF6600?style=flat-square)
![Scikit--Learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square)
![Excel](https://img.shields.io/badge/-Excel-217346?logo=microsoft-excel&logoColor=white&style=flat-square)

**[🌐 Try the Live App](https://your-ltv-app.streamlit.app)** &nbsp;·&nbsp;
**[📓 Open Notebook](./project-1-ltv/Customer_LTV_Prediction.ipynb)** &nbsp;·&nbsp;
**[📄 Read Report](./project-1-ltv/LTV_Project_Report.pdf)** &nbsp;·&nbsp;
**[📊 Excel Report](./project-1-ltv/LTV_Excel_Report.xlsx)**

</div>

<br/>

### 💡 The Problem

> Most businesses treat all customers the same.
> They spend equally on someone who'll buy ₹50,000 worth next year
> and someone who'll never return.
> **This model tells them apart — before a single rupee is spent.**

<br/>

### 🔬 How It Works

```
  RAW TRANSACTIONS (541,909 rows)
           │
           ▼
  ┌─────────────────────────────────┐
  │  DATA CLEANING                  │
  │  Remove nulls · cancellations   │
  │  Compute TotalPrice             │
  └───────────────┬─────────────────┘
                  │
        ┌─────────┴──────────┐
        ▼                    ▼
   FEATURE WINDOW        TARGET WINDOW
   (First 6 months)      (Next 6 months)
   Build inputs      →   Measure actual spend
        │
        ▼
  ┌─────────────────────────────────┐
  │  RFM FEATURE ENGINEERING        │
  │  R  Recency  (days since buy)   │
  │  F  Frequency (# orders)        │
  │  M  Monetary (total ₹ spent)    │
  │  +  AOV · Tenure · UniqueProds  │
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  XGBOOST REGRESSOR              │
  │  200 trees · LR 0.05 · Depth 4  │
  │  MAE ₹124 · RMSE ₹298 · R²0.847│
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  4-TIER SEGMENTATION            │
  │  ⭐ VIP · 🔵 High · 🔷 Med · ⚪Low│
  └─────────────────────────────────┘
```

<br/>

### 📊 Results

<div align="center">

| Metric | XGBoost | Random Forest | Winner |
|:---:|:---:|:---:|:---:|
| MAE | **₹124.50** | ₹178.30 | 🥇 XGBoost |
| RMSE | **₹298.70** | ₹412.50 | 🥇 XGBoost |
| R² Score | **0.847** | 0.791 | 🥇 XGBoost |
| Accuracy ±20% | **81.2%** | 74.5% | 🥇 XGBoost |

</div>

<br/>

### 🎯 Customer Segments

```
 ⭐  VIP      ████████████████████  Avg ₹2,350  Top 12.5%  Loyalty rewards · Early access
 🔵  High     ████████████████      Avg ₹890    Top 25%    Upsell · Premium bundles
 🔷  Medium   ████████              Avg ₹380    Top 50%    Re-engagement campaigns
 ⚪  Low      ████                  Avg ₹75     Bottom     Low-cost retention only
```

> 💡 **The top 12.5% of customers generate 10× the LTV of the bottom 25%.**

<br/>

### 📁 Feature Importance

```
 Monetary      ██████████████████████████████████  34.2%  ← #1 — past spend drives future spend
 Recency       ████████████████████████            22.8%  ← recent buyers come back
 Frequency     ███████████████████                 18.7%  ← order count signals loyalty
 Tenure        ████████████                        11.2%  ← longer relationship = more value
 AOV           █████████                            8.1%  ← high avg order = premium buyer
 Unique Prods  ██████                               5.0%  ← product variety = engagement
```

<br/>

### 🗂 Project Files

```
📦 project-1-ltv/
├── 📓 Customer_LTV_Prediction.ipynb   10-step ML notebook (run top to bottom)
├── 🌐 app.py                          Streamlit app — Glassmorphism UI
├── 📊 LTV_Excel_Report.xlsx           4-sheet Excel: Predictions·Segments·RFM·Metrics
├── 📽️  LTV_Presentation.pptx          8-slide dark-theme portfolio deck
├── 📄 LTV_Project_Report.pdf          2-page formal project report
├── 🤖 ltv_model.pkl                   Trained XGBoost model (after running notebook)
└── 📋 requirements.txt                Python dependencies
```

### ⚡ Quick Start

```bash
cd project-1-ltv
pip install -r requirements.txt
# Download OnlineRetail.xlsx from Kaggle → place here
jupyter notebook Customer_LTV_Prediction.ipynb
streamlit run app.py
```

<br/>

---

<br/>

<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PROJECT  2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

# ⚡ EV Charging Demand Forecasting

</div>

<div align="center">

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![Prophet](https://img.shields.io/badge/-Prophet-0668E1?style=flat-square)
![ARIMA](https://img.shields.io/badge/-ARIMA-7B61FF?style=flat-square)
![Scipy](https://img.shields.io/badge/-Scipy-8CAAE6?logo=scipy&logoColor=white&style=flat-square)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?logo=tableau&logoColor=white&style=flat-square)

**[📊 Live Tableau Dashboard](https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)** &nbsp;·&nbsp;
**[📓 Open Notebook](./project-2-ev/EV_Charging_Notebook.ipynb)** &nbsp;·&nbsp;
**[📄 Read Report](./project-2-ev/EV_Project_Report.pdf)**

</div>

<br/>

### 💡 The Problem

> India's EV market is growing fast — but charging stations face unpredictable
> congestion at peak hours, wasting grid capacity and frustrating users.
> **This model predicts demand 30 days ahead so operators can plan,
> and users can charge without the wait.**

<br/>

### 🔬 How It Works

```
  RAW HOURLY DATA (43,800 rows · 5 stations · 1 year)
           │
           ▼
  ┌──────────────────────────────────────────────┐
  │  FEATURE ENGINEERING                          │
  │  Time  → hour · weekday · month · is_weekend  │
  │  Weather → temperature · rainfall · wind      │
  │  Station → capacity · city · utilisation %    │
  └──────────────────┬───────────────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   ┌─────────────┐       ┌─────────────────┐
   │   ARIMA     │       │    PROPHET       │
   │  (2, 1, 2)  │       │  Multiplicative  │
   │  Baseline   │       │  Seasonality     │
   │  MAE 0.412  │       │  MAE 0.298 ✅   │
   └─────────────┘       └────────┬────────┘
                                  │
                    ┌─────────────┴──────────────┐
                    ▼                            ▼
           ANOMALY DETECTION           OPTIMIZATION ENGINE
           Z-score > 3.0               Top 5 slots by
           Flags spikes & drops        availability %
```

<br/>

### 📊 Model Comparison

<div align="center">

| Model | MAE | RMSE | Auto Seasonality | Holiday Support | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ARIMA(2,1,2) | 0.412 | 0.587 | ❌ Manual | ❌ | Baseline |
| **Prophet** | **0.298** | **0.431** | ✅ Auto | ✅ | **Production Model** |

</div>

<br/>

### 📈 Demand Patterns Uncovered

```
  Time of Day          Avg Utilisation    Pattern
  ───────────────────────────────────────────────────────────
  12 AM – 5 AM   ░░░░░░░░░░░░░░░░░░░░░░   8%   Night idle
   6 AM – 7 AM   ░░░░░░░░░░░░░░░░░░████  35%   Pre-commute
   7 AM – 9 AM   ████████████████████████ 80%  ⚠️  MORNING PEAK
  10 AM – 11 AM  ░░░░░░░░░░░░░░████████  50%   Mid-morning
  11 AM –  1 PM  ░░░░░░░░░░░░░░░░░█████  65%   Lunch window
   2 PM –  4 PM  ░░░░░░░░░░░░░░░░░░░███  40%   Afternoon dip
   5 PM –  8 PM  ████████████████████████ 90%  🔴 EVENING PEAK
   9 PM – 11 PM  ░░░░░░░░░░░░░░░░███████ 20%   Wind-down
```

<br/>

### 🚀 Bonus Features

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  🔴  ANOMALY DETECTION                                          │
│      Method   : Z-score per station (threshold > 3.0)          │
│      Detects  : Demand spikes (events, cable faults)            │
│                 Demand drops  (outages, road closures)          │
│      Output   : EV_Anomaly_Report.csv                          │
│      Evaluated: Precision · Recall · F1 Score                  │
│                                                                 │
│  ⚡  CHARGING OPTIMIZATION ENGINE                               │
│      Input    : city · date · preferred hours                   │
│      Logic    : Rank slots by availability %                    │
│      Output   : ⭐ Best Slot / ✅ Good / 🔶 Moderate            │
│      File     : EV_Optimization_Strategy.csv                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

<br/>

### 📊 Live Tableau Dashboard

```
🔗 https://public.tableau.com/views/EVChargingDemandForecastingTableaudashboard/Dashboard1

Contains:
  🟣  Demand Heatmap    Hour × Weekday intensity grid
  📈  Monthly Trend     Seasonal demand curve across 12 months
  ⚡  Station Compare   Utilisation % per station (bar chart)
  🌡️   Weather Impact   Temperature & rainfall vs demand scatter
  🔴  Anomaly Markers  Flagged unusual spikes overlaid on timeline
```

<br/>

### 🗂 Project Files

```
📦 project-2-ev/
├── 📓 EV_Charging_Notebook.ipynb      10-step forecasting notebook
├── 📊 EV_Charging_Demand.csv          Raw dataset (43,800 rows)
├── 📊 EV_Tableau_Ready.csv            Aggregated CSV — Tableau data source
├── 📊 EV_Anomaly_Report.csv           Detected anomalies with z-scores
├── 📊 EV_Optimization_Strategy.csv    Best charging slots per city
├── 📈 EV_Excel_Report.xlsx            Station performance Excel report
├── 📄 EV_Project_Report.pdf           2-page formal project report
└── 📋 requirements.txt                Python dependencies
```

### ⚡ Quick Start

```bash
cd project-2-ev
pip install -r requirements.txt
jupyter notebook EV_Charging_Notebook.ipynb
# Open EV_Tableau_Ready.csv in Tableau Public for the dashboard
```

> ⚠️ **Use Python 3.10 or 3.11.** Python 3.13 has compatibility issues with Prophet and statsmodels.

<br/>

---

<br/>

## 🧰 Combined Tech Stack

<div align="center">

| Layer | Project 1 — LTV | Project 2 — EV |
|:---:|:---:|:---:|
| **Language** | Python 3.9+ | Python 3.11 |
| **Core Model** | XGBoost Regressor | ARIMA + Prophet |
| **Features** | RFM + Tenure + AOV | Weather + Temporal |
| **Validation** | MAE · RMSE · R² | MAE · RMSE · Precision-Recall |
| **Bonus** | Segmentation + Streamlit App | Anomaly Detection + Optimizer |
| **Dashboard** | Streamlit (Live) | Tableau Public (Live) |
| **Reports** | Excel 4-sheet + PPTX 8-slide | Excel + 4 CSVs |
| **PDF Report** | ✅ 2-page | ✅ 2-page |

</div>

<br/>

---

## 📁 Full Repository Structure

```
📦 data-science-portfolio/
│
├── 📄 README.md                            ← You are here
│
├── 📁 project-1-ltv/
│   ├── 📓 Customer_LTV_Prediction.ipynb
│   ├── 🌐 app.py
│   ├── 📊 LTV_Excel_Report.xlsx
│   ├── 📽️  LTV_Presentation.pptx
│   ├── 📄 LTV_Project_Report.pdf
│   └── 📋 requirements.txt
│
└── 📁 project-2-ev/
    ├── 📓 EV_Charging_Notebook.ipynb
    ├── 📊 EV_Charging_Demand.csv
    ├── 📊 EV_Tableau_Ready.csv
    ├── 📊 EV_Anomaly_Report.csv
    ├── 📊 EV_Optimization_Strategy.csv
    ├── 📈 EV_Excel_Report.xlsx
    ├── 📄 EV_Project_Report.pdf
    └── 📋 requirements.txt
```

<br/>

---

## 🗺️ Roadmap

<div align="center">

| Status | Feature |
|:---:|:---|
| ✅ Done | LTV Prediction — XGBoost + RFM Pipeline |
| ✅ Done | LTV Streamlit App — Glassmorphism UI |
| ✅ Done | LTV Excel 4-sheet Report + PPTX Deck |
| ✅ Done | EV Forecasting — ARIMA + Prophet |
| ✅ Done | EV Anomaly Detection — Z-score Engine |
| ✅ Done | EV Optimization Engine — Best Slot Recommender |
| ✅ Done | EV Live Tableau Dashboard |
| ⬜ Next | SHAP Explainability for LTV model |
| ⬜ Next | BG/NBD Probabilistic CLV Model |
| ⬜ Next | Live Weather API Integration for EV |
| ⬜ Next | LSTM Deep Learning Comparison |
| ⬜ Next | Combined Multi-Project Streamlit Portfolio App |

</div>

<br/>

---

<div align="center">

**Built from scratch. Deployed live. Ready to present.**

*If this helped you, drop a ⭐ — it genuinely means a lot!*

<br/>

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=140&section=footer&animation=fadeIn" width="100%"/>
