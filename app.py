import streamlit as st
import pandas as pd
import pickle
from booking import book_class

# ---------------- LOAD MODEL ----------------
with open("models.pkl", "rb") as f:
    model, label_encoders, target_encoder, scaler = pickle.load(f)

# ---------------- LOAD DATA ----------------
classes_df = pd.read_csv("classes_compressed.csv")

# ---------------- UI ----------------
st.title("🏋️ FitBot AI - Gym Chatbot")
st.caption("AI-powered Gym Membership Chatbot with Intelligent Schedule Compression")

st.write("Enter your fitness details to get class recommendations.")

# ---------------- USER INPUT ----------------
age = st.number_input("Age", 18, 60, 25)
bmi = st.number_input("BMI", 15.0, 40.0, 22.0)
goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Flexibility"])
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
attendance = st.slider("Weekly Attendance", 0, 5, 2)
preferred_time = st.selectbox("Preferred Time", ["Morning", "Evening"])

# ---------------- RECOMMENDATION ----------------
if st.button("Get Recommendation"):

    input_data = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "fitness_goal": goal,
        "experience_level": experience,
        "weekly_attendance": attendance,
        "preferred_time": preferred_time
    }])

    # Encode categorical features
    for col in ["fitness_goal", "experience_level", "preferred_time"]:
        input_data[col] = label_encoders[col].transform(input_data[col])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    class_name = target_encoder.inverse_transform(prediction)[0]

    st.success(f"Recommended Class: {class_name}")

    # Safe match (avoid crash)
    class_info = classes_df[
        classes_df["class_name"].str.strip() == class_name.strip()
    ]

    if class_info.empty:
        st.error("Class information not found in database.")
    else:
        st.write("### Compressed Class Description:")
        st.write(class_info["compressed_description"].values[0])

        # Booking button
        if st.button("Book This Class"):
            result = book_class(999, class_name)
            st.info(result)

    # Display project metrics
    st.markdown("---")
    st.metric("Model Type", "Logistic Regression")
    st.metric("Compression Method", "Gemini-based Summarization")
    st.markdown("### 📊 System Performance")
    st.metric("Classes Available", len(classes_df))
    st.metric("Users Simulated", 500)