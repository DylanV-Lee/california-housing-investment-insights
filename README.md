# 🏠 California Housing Investment Opportunity Analysis

**Using data science to identify high-potential real estate investment zones in California**

---

## 🚀 Project Overview

**Business Goal:** Help a real estate investment firm grow revenue by identifying undervalued regions in California to maximize ROI from property flips or rentals.  
**Data Science Goal:** Build a pricing intelligence model using historical sales data to estimate fair house prices and compare those against current market prices to flag undervalued blocks.

---

## 🏢 Business Context

- **Client:** HomeVision – a data-driven real estate investment firm  
- **Strategy:** Buy low → Renovate → Sell/Rent → Reinvest profits  
- **Challenge:** Firms often lack scalable tools to pinpoint areas where the current market undervalues properties relative to their potential  

---

## 💼 Business Problem Statement

> _“Which residential blocks in California are currently priced below their estimated fair value, based on past sale trends and demographic features, and should be prioritized for acquisition?”_

This solution enables analysts and field scouts to prioritize areas with the highest investment potential — reducing guesswork and accelerating research workflows.

---

## 📊 Business Metrics

| Metric                     | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| **Undervaluation Gap ($)** | Difference between predicted price and actual price         |
| **Lead Score**             | Normalized score based on undervaluation and local income  |
| **# of Investment Leads**  | Count of high-potential zones flagged                     |
| **Map Coverage (%)**       | Percent of regions evaluated                              |
| **(Planned) Avg ROI**      | Measured post-acquisition by business team               |

---

## 🧠 Data Science Approach

### 🔹 Dataset

- **Source:** California Housing Dataset (~20,640 block groups)  
- **Target Variable:** `MedHouseVal` – median house value per group

### 🔹 Key Features

- `MedInc` – Median income (proxy for demand)  
- `HouseAge`, `AveRooms`, `AveBedrms`, `AveOccup`  
- `Latitude`, `Longitude`, `Population`

---

## 🔍 Methodology

1. **Preprocessing**
   - Feature engineering (e.g., room-to-bedroom ratio)
   - Geo-transformations for location-based features

2. **Model Training**
   - Regressor: **Random Forest**
   - Evaluation Metrics: **RMSE**, **R²**

3. **Opportunity Scoring**
   - Gap = Predicted Price − Actual Price
   - Filter for significant positive gaps
   - Rank leads by gap size & local income

4. **Reporting & Mapping**
   - Generate heatmaps for high-lead zones
   - Deliver lead tables with investment scores

---

## 📍 Key Deliverables

- ✅ Predictive model estimating fair market values  
- ✅ Dashboard to aid business decision-making  
- ✅ Undervaluation heatmap across California  
- ✅ Ranked list of top investment block groups  
- ✅ Quantified price deviation vs. current market  

---

## 🧭 Assumptions & Limitations

| Assumption                     | Note                                                                 |
|--------------------------------|----------------------------------------------------------------------|
| **Regional modelling**         | Insights are at the block group level, not individual property level |
| **1990s data**                 | Based on a historical public dataset, not live market data           |
| **train.csv = past data**      | Simulates firm's internal historical sales record                    |
| **test.csv = current prices**  | Simulates present-day market prices for scoring                    |
| **Same feature distributions** | Assumes similar feature behavior between train and test sets    |
| **Uniform renovation cost**    | Renovation costs not explicitly modeled in ROI                      |
| **Simulated scenario**         | Built using public datasets to simulate real-world strategy          |

---

## 📈 Sample Output

| Block Group | Actual Price  | Predicted Price  | Gap ($) | Income | Lead Score |
|-------------|---------------|------------------|---------|--------|------------|
| Group A     | $140,000      | $220,000         | $80,000 | $6.5k  | 0.95       |
| Group B     | $200,000      | $270,000         | $70,000 | $7.1k  | 0.91       |

🗺️ **Heatmap:** Red zones indicate top investment opportunities.

---

## 🛠️ Technologies Used

- **Languages/Tools:** Python, Jupyter Notebooks, VS Code  
- **Libraries:** `pandas`, `scikit-learn`, `seaborn`, `matplotlib`, `folium`  
- **Versioning:** Git & GitHub  

---

## 🧩 Business Impact

This project empowers faster and smarter real estate decisions. It helps investment teams:

- Flag high-opportunity areas algorithmically  
- Reduce reliance on manual research  
- Accelerate field scouting  
- Improve ROI by focusing only on the most viable leads  
- Visualize insights geographically for strategic decision-making  

---

## 🚧 Next Steps

- Integrate external data sources (e.g., crime rates, school ratings, rental yields)  
- Incorporate renovation cost models to compute ROI more realistically  
- Explore time-series forecasting for property value trends  

---

📫 _Have ideas? Feel free to fork and contribute!_
