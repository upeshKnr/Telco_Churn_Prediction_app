import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/Telco_churn_RFmodel.pkl")
features = joblib.load("models/Telco_X_features.pkl")

# Load CSS file 
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<h1>Telco Churn Prediction Dashboard</h1>
<p style='text-align:center; color:gray;'>Predict whether a customer will churn or not</p>
""", unsafe_allow_html=True)


# Sidebar for user input
st.sidebar.header("Customer Details")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges", 0, 150, 50)

contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment_method = st.sidebar.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer", "Credit card"
])

paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
senior = st.sidebar.selectbox("Senior Citizen", [0,1])



input_df = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("### 📋 Customer Input Summary")
st.dataframe(input_df)

st.markdown('</div>', unsafe_allow_html=True)

############################################

# Convert input to dataframe
input_dict = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "SeniorCitizen": senior,
    "PaperlessBilling": 1 if paperless == "Yes" else 0,
}

input_df = pd.DataFrame([input_dict])

# Align with training features
input_df = input_df.reindex(columns=features, fill_value=0)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.markdown('<div class="error-box">⚠️ High Risk: Customer Likely to Churn</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="success-box">✅ Low Risk: Customer Likely to Stay</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)


prob = model.predict_proba(input_df)[0][1]
st.write(f"Churn Probability: {prob:.2f}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">Model: Random Forest</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">Focus: Recall</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">Use Case: Retention Strategy</div>', unsafe_allow_html=True)


