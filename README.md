# Telco Customer Churn Prediction

A telecom company is losing 26% of its customers annually. This project 
identifies the key drivers of churn and builds a machine learning model 
to flag at-risk customers before they leave — enabling targeted retention 
campaigns that protect revenue.

---

## Business problem
Customer acquisition costs 5-7x more than retention. Identifying which 
customers are likely to churn — before they do — allows the business to 
intervene with targeted offers at the right moment.

---

## What I built
- **Exploratory Data Analysis** — uncovered the key behavioral and 
  contractual patterns that predict churn
- **Machine Learning Model** — trained and compared 3 models, achieving 
  AUC 0.835 with Logistic Regression
- **Risk Scoring System** — scored all 7,032 customers into High / Medium 
  / Low risk segments
- **Actionable deliverable** — exported a prioritized list of 1,039 
  high-risk customers ready for retention action

---

## Key findings

| Driver | Insight |
|--------|---------|
| Contract type | Month-to-month customers churn at 42.7% vs 2.8% on 2-year contracts |
| Tenure | 50% of churners leave within the first 6 months |
| Monthly charges | Churned customers pay $75-100/month — high bill, low loyalty |
| Add-ons | No tech support or security = ~42% churn vs ~15% with them |
| Payment method | Electronic check customers churn at 45.3% — highest of any group |

---

## Model results

| Model | AUC Score |
|-------|-----------|
| Logistic Regression | **0.835** |
| Random Forest | 0.813 |
| XGBoost | 0.805 |

---

## Risk segmentation

| Segment | Customers | Avg Churn Probability |
|---------|-----------|----------------------|
| High risk | 1,039 | 69.1% |
| Medium risk | 1,666 | 44.9% |
| Low risk | 4,327 | 9.6% |

**Business impact:** Converting just 20% of high-risk customers to annual 
contracts protects ~$228,000 in annual revenue.

---

## Project structure
```
bank-project/
├── data/
│   └── raw/                  ← source data (not tracked in git)
├── notebooks/
│   ├── 01_eda.ipynb          ← exploratory data analysis
│   └── 02_model.ipynb        ← churn prediction model
├── outputs/
│   ├── figures/              ← all charts and visualizations
│   └── reports/              ← churn risk scores CSV
├── src/
│   └── utils.py              ← reusable data loading functions
└── requirements.txt
```

---

## Setup
```bash
git clone https://github.com/zeyadElshazly1/telco-churn-prediction.git
cd telco-churn-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Then download the dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) 
and place it at `data/raw/telco_churn.csv`.

---

## Tech stack
Python, Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn

---

## Next steps
- Add SHAP explainability to show WHY each customer is flagged
- Build a Power BI dashboard connected to the risk scores
- Add automated weekly retraining pipeline