<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=7B61FF&height=200&section=header&text=Customer%20LTV%20Predictor&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Predict%20%C2%B7%20Segment%20%C2%B7%20Retain&descAlignY=58&descAlign=50" width="100%"/>

<br/>

<!-- BADGES -->
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Report-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

<br/>

<!-- DEMO LINK -->
### 🌐 [Live Demo →](https://customer-ltv-predictor.streamlit.app/) &nbsp;&nbsp; 📓 [View Notebook →](#) &nbsp;&nbsp; 📊 [See Report →](#)

<br/>

> *"Not all customers are equal — this model finds the ones worth fighting for."*

</div>

---

<br/>

## 🧠 What is This?

<table>
<tr>
<td width="60%">

A **machine learning system** that predicts how much each customer will spend in the next 6 months — before they spend it.

Built on **RFM feature engineering** (Recency, Frequency, Monetary) and a tuned **XGBoost regression model**, it segments customers into 4 actionable tiers so marketing teams can allocate budgets where they'll actually work.

**The problem it solves:** Most businesses treat all customers the same. This model proves they shouldn't.

</td>
<td width="40%" align="center">

```
Given a customer's past behaviour:

  Recency   ──┐
  Frequency ──┼──► XGBoost ──► £ LTV Score
  Monetary  ──┘         │
  Tenure    ──┘         └──► Segment
  AOV       ──┘               (VIP / High /
  Products  ──┘                Medium / Low)
```

</td>
</tr>
</table>

<br/>

---

## 📊 Results at a Glance

<div align="center">

| Metric | XGBoost | Random Forest | Winner |
|:---:|:---:|:---:|:---:|
| MAE | **£124.50** | £178.30 | 🥇 XGBoost |
| RMSE | **£298.70** | £412.50 | 🥇 XGBoost |
| R² Score | **0.847** | 0.791 | 🥇 XGBoost |
| Accuracy (±20%) | **81.2%** | 74.5% | 🥇 XGBoost |
| Training Time | **2.4s** | 8.1s | 🥇 XGBoost |

</div>

<br/>

---

## ✨ Customer Segments

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ⭐ VIP          │  Avg LTV: £2,350  │  Top 12.5%  │  5 customers  │
│  ─────────────────────────────────────────────────────────────────  │
│  → Exclusive loyalty rewards · Early product access · Dedicated mgr │
│                                                                     │
│  🔵 HIGH         │  Avg LTV: £890    │  Top 25%    │  10 customers │
│  ─────────────────────────────────────────────────────────────────  │
│  → Upsell premium bundles · Subscription offers · Cross-sell        │
│                                                                     │
│  🔷 MEDIUM       │  Avg LTV: £380    │  Top 50%    │  15 customers │
│  ─────────────────────────────────────────────────────────────────  │
│  → Personalised re-engagement emails · Timed discount campaigns     │
│                                                                     │
│  ⚪ LOW          │  Avg LTV: £75     │  Bottom 50% │  10 customers │
│  ─────────────────────────────────────────────────────────────────  │
│  → Low-cost retention only · Remove from paid channels              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

<br/>

---

## 🗂️ Project Structure

```
📦 customer-ltv-predictor/
│
├── 📓 Customer_LTV_Prediction.ipynb   ← Full 10-step ML notebook
├── 🌐 app.py                          ← Streamlit web app 
├── 📊 LTV_Excel_Report.xlsx           ← 4-sheet Excel report
├── 📽️  LTV_Presentation.pptx          ← 8-slide portfolio deck
├── 📁 outputs 
           └──  Final_LTV_Predictions.csv        ← Output: customer LTV + segments
           └──  Segment_Summary.csv              ← Output: segment-level aggregations
           └──  ltv_model.pkl                    ← Trained XGBoost model
├── 📋 LTV Project Report.pdf                              
├── 📋 requirements.txt                ← Python dependencies
└── 📄 README.md                       ← You are here
```

<br/>

---

## ⚙️ How It Works — Step by Step

```
STEP 1          STEP 2          STEP 3          STEP 4          STEP 5
  │               │               │               │               │
Load &        Timeline         Feature          Train           Segment
Clean Data  →  Split       →  Engineering  →  XGBoost     →  Customers
  │               │               │               │               │
Remove         First 6M        R  Recency        200 trees       VIP
nulls &    →   = features  →   F  Frequency  →   LR: 0.05   →   High
returns        Next  6M        M  Monetary       Depth: 4        Medium
               = target        +  AOV                            Low
                               +  Tenure
                               +  UniqueProds
```

<br/>

---

## 🚀 Quick Start

### 1️⃣ Clone & Install

```bash
git clone https://github.com/your-username/customer-ltv-predictor.git
cd customer-ltv-predictor
pip install -r requirements.txt
```

### 2️⃣ Get the Dataset

Download **OnlineRetail.xlsx** from [Kaggle – UCI Online Retail](https://www.kaggle.com/datasets/vijayuv/onlineretail) and place it in the project root.

### 3️⃣ Run the Notebook

```bash
jupyter notebook Customer_LTV_Prediction.ipynb
```

> Run all cells top to bottom. This generates `ltv_model.pkl`, `Final_LTV_Predictions.csv`, and `Segment_Summary.csv`

### 4️⃣ Launch the Web App

```bash
streamlit run app.py
```

🎉 App opens at `http://localhost:8501`

<br/>

---

## 🧪 Feature Importance

```
Monetary      ████████████████████████████████████  34.2%  ← #1 driver
Recency       ████████████████████████             22.8%
Frequency     ███████████████████                  18.7%
Tenure        ████████████                         11.2%
AOV           █████████                             8.1%
Unique Prods  ██████                                5.0%
```

> 💡 **Insight:** A customer who spent more in the past AND bought recently is the strongest predictor of high future LTV — even stronger than how often they buy.

<br/>

---

## 🌐 Web App Features

```
┌──────────────────── Glassmorphism UI ────────────────────────┐
│                                                              │
│  🎚️  6 RFM sliders  →  real-time AOV computation            │
│                                                              │
│  ⚡  Instant LTV prediction  →  loads your trained model     │
│                                                              │
│  🎯  Segment badge  →  VIP / High / Medium / Low            │
│                                                              │
│  📊  RFM breakdown bars  →  visual score per dimension      │
│                                                              │
│  💡  Marketing action card  →  what to do with this customer │
│                                                              │
│  📈  LTV gauge chart  →  gradient arc visualisation         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

<br/>

---

## 📦 Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:---:|:---:|:---:|
| Language | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Core |
| Data | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) | Cleaning & RFM |
| ML | ![XGBoost](https://img.shields.io/badge/-XGBoost-FF6600?style=flat-square) | LTV regression |
| Validation | ![Sklearn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square) | MAE, RMSE, R² |
| Viz | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square) ![Seaborn](https://img.shields.io/badge/-Seaborn-4C72B0?style=flat-square) | Charts & plots |
| App | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square) | Web UI |
| Report | ![Excel](https://img.shields.io/badge/-Excel-217346?logo=microsoft-excel&logoColor=white&style=flat-square) | Business output |

</div>

<br/>

---

## 📈 Key Business Insights

> **1. The top 12.5% of customers generate 10× the LTV of the bottom 25%**
> Concentrating retention spend on VIP and High segments dramatically outperforms blanket campaigns.

> **2. Recency beats frequency**
> A customer who bought once last week is a better prospect than one who bought 20 times last year but hasn't been seen since.

> **3. Medium segment is the biggest growth lever**
> 37.5% of your base — already engaged, just needs a personalised nudge to become High value.

<br/>

---

## 🗺️ Roadmap / Bonus Extensions

- [x] XGBoost regression model
- [x] RFM feature engineering
- [x] 4-tier customer segmentation
- [x] Streamlit web app
- [x] Excel 4-sheet report
- [ ] SHAP explainability layer
- [ ] BG/NBD probabilistic CLV model
- [ ] Churn probability score per customer
- [ ] Email campaign ROI simulator
- [ ] Real-time database integration

<br/>

---

## 👤 About

<div align="center">

**Built as part of a Data Science Portfolio Project**

If you found this useful, please ⭐ star the repo!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/architha-k-a22b4539a)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ARCHITHAK-DS)

</div>

<br/>

<!-- FOOTER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=7B61FF&height=120&section=footer&animation=fadeIn" width="100%"/>

