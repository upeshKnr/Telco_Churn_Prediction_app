## 📊 Telco Customer Churn Prediction App

This project is an end-to-end machine learning solution designed to predict customer churn in a telecom company. The objective is to identify high-risk customers and provide actionable insights to improve retention strategies.

---

## 🚀 Key Features

* 🔍 Comprehensive Exploratory Data Analysis (EDA) with business-driven insights
* 🧠 Feature engineering focused on customer behavior, service usage, and financial patterns
* 🤖 Machine Learning models (Logistic Regression, Random Forest, XGBoost) with performance comparison
* 📈 Model evaluation using precision, recall, F1-score, and ROC-AUC
* 🎯 Focus on recall optimization to effectively capture churn cases
* 💻 Interactive Streamlit web application with custom UI/UX
* 📦 Model deployment using saved artifacts (model + feature schema)

---

## 🧠 Business Insights

* Customers on month-to-month contracts show significantly higher churn rates
* High monthly charges correlate with increased churn probability
* Early-stage customers (low tenure) are more likely to churn
* Higher service engagement reduces churn risk

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn, XGBoost
* Seaborn, Matplotlib
* Streamlit
* Joblib

---

## 📊 Use Case

This application can help telecom companies:

* Identify customers at high risk of churn
* Design targeted retention campaigns
* Optimize pricing and subscription strategies
* Improve early customer engagement

---

## ⚙️ How to Run

```bash
git clone <your-repo-link>
cd Telco_Churn_Prediction_app
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Project Structure

```
Telco_Churn_Prediction_app/
│
├── app.py
├── models/
├── dataset/
├── notebooks/
├── assets/
└── requirements.txt
```

---

## 🎯 Future Improvements

* Hyperparameter tuning and model optimization
* Deployment on cloud platforms
* Real-time data integration
* Advanced explainability (SHAP / LIME)

---

## 💡 Author

Developed as part of a data science portfolio project to demonstrate end-to-end ML workflow, from data analysis to deployment.
