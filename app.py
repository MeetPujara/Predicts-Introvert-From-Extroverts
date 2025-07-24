import streamlit as st
import joblib
import numpy as np

# Load saved model and scaler
model = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')

# Page setup
st.set_page_config(page_title="Introvert/Extrovert Classifier", layout="centered")
st.title("🧠 Predict Your Personality Type")
st.markdown("This app predicts whether you're an **Introvert** or **Extrovert** based on your behavioral traits.")

st.markdown("---")

# Input fields matching the training data
time_spent_alone = st.slider("Time Spent Alone (hours/day)", 0.0, 24.0, 5.0, step=0.5)
stage_fear = st.selectbox("Do You Have Stage Fear?", ["Yes", "No"])
stage_fear_encoded = 1 if stage_fear == "Yes" else 0

social_event_attendance = st.slider("Social Event Attendance (per month)", 0, 30, 4)
going_outside = st.slider("Days Going Outside (per week)", 0, 7, 3)
drained_after_socializing = st.selectbox("Do You Feel Drained After Socializing?", ["Yes", "No"])
drained_encoded = 1 if drained_after_socializing == "Yes" else 0

friends_circle_size = st.slider("Number of Close Friends", 0, 50, 5)
post_frequency = st.slider("Social Media Post Frequency (per week)", 0, 20, 2)

# Prediction button
if st.button("Predict Personality"):
    input_data = np.array([[time_spent_alone, stage_fear_encoded, social_event_attendance,
                            going_outside, drained_encoded, friends_circle_size, post_frequency]])
    
    input_scaled = scaler.transform(input_data)
    label_map = {0: "Introvert", 1: "Extrovert"}
    prediction = model.predict(input_scaled)[0]
    st.success(f"You are likely an **{label_map[prediction]}**.")
