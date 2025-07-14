import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("xgb_heart_model.pkl")

model = load_model()

st.title("❤️ Heart Disease Predictor")

st.sidebar.header("Patient Info")

def user_input():
    age = st.sidebar.number_input("Age", 1, 120, 50)
    sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
    cp = st.sidebar.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.sidebar.number_input("Resting BP", value=120)
    chol = st.sidebar.number_input("Cholesterol", value=200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120", [0, 1])
    restecg = st.sidebar.selectbox("Rest ECG (0–2)", [0, 1, 2])
    thalach = st.sidebar.number_input("Max Heart Rate", value=150)
    exang = st.sidebar.selectbox("Exercise-Induced Angina", [0, 1])
    oldpeak = st.sidebar.number_input("Oldpeak", value=1.0)
    slope = st.sidebar.selectbox("Slope (0–2)", [0, 1, 2])
    ca = st.sidebar.selectbox("Major Vessels Colored (0–3)", [0, 1, 2, 3])
    thal = st.sidebar.selectbox("Thal (0=normal, 1=fixed, 2=reversable)", [0, 1, 2])
    
    sex = 1 if sex == "Male" else 0
    
    data = {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,
        'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach,
        'exang': exang, 'oldpeak': oldpeak, 'slope': slope,
        'ca': ca, 'thal': thal
    }
    return pd.DataFrame([data])

input_df = user_input()

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease (Confidence: {proba:.2f})")
    else:
        st.success(f"✅ Low Risk of Heart Disease (Confidence: {proba:.2f})")
