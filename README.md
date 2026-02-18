# fitness
FitBot AI
AI-Powered Gym Membership Chatbot with Intelligent Schedule Compression
📌 Project Overview
FitBot AI is an intelligent gym membership chatbot that provides personalized fitness class recommendations, compresses verbose class descriptions using Generative AI, and automates class booking with capacity handling.
The system integrates:
Machine Learning for class recommendation
Gemini-based NLP compression for schedule optimization
Booking logic with capacity simulation
Interactive chatbot interface using Streamlit
This project demonstrates the practical integration of ML and GenAI in a real-world fitness management scenario.

Problem Statement
Modern gyms face several operational challenges:
Overloaded front desk staff
Manual booking inefficiencies
Long, verbose class descriptions
Lack of personalized class recommendations
Low member engagement
There is a need for an AI-driven system that can:
Recommend classes based on user profile
Compress class schedules for faster readability
Automate booking
Improve user experience

💡 Proposed Solution
FitBot AI provides:
1️⃣ Personalized class recommendation using Logistic Regression
2️⃣ Intelligent schedule compression using Gemini API
3️⃣ Real-time booking simulation with capacity handling
4️⃣ Interactive chatbot interface
The system reduces textual payload, automates decision-making, and improves scalability.

🏗 System Architecture
User Input (Streamlit UI)
↓
Feature Encoding & Scaling
↓
Logistic Regression Model
↓
Predicted Class
↓
Compressed Description (Gemini Processed)
↓
Booking Engine (Capacity + Confirmation)

🧠 Machine Learning Approach
Model Used:
Logistic Regression (Multi-class Classification)
Features Used:
Age
BMI
Fitness Goal
Experience Level
Weekly Attendance
Preferred Time

Why Logistic Regression?
Lightweight
Interpretable
Fast training
Suitable for small-to-medium datasets
Easy deployment

🤖 Generative AI Component
Model Used:
Gemini (Flash Variant)
Purpose:
Compress long class descriptions into short, meaningful summaries.
Example:
Original:
Energetic cardio workout designed to improve heart health and calorie burning.
Compressed:
Cardio session focused on heart health and calorie burn.
Benefits:
Reduced description size
Faster chatbot response
Improved user readability

📊 Booking Engine
The booking system:
Checks class capacity
Simulates successful booking
Handles cancellation
Designed for waitlist expansion (future scope)

🗂 Dataset Description
Users Dataset (500 simulated users)
Demographics
Fitness preferences
Historical class mapping
Classes Dataset
Class name
Duration
Intensity
Trainer
Capacity
Description
Trainers Dataset
Specialization
Experience
Rating
Trainer data is included to support future personalization enhancements.

🛠 Tech Stack
Python
Scikit-learn
Pandas
Streamlit
Gemini API
Pickle (model persistence)

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install streamlit pandas scikit-learn google-genai
2️⃣ Generate Dataset
python generate_data.py
3️⃣ Train Recommendation Model
python recommendation_model.py
4️⃣ Run Streamlit App
python -m streamlit run app.py

📈 System Performance Indicators
500 simulated users
7 fitness classes
ML-based recommendation
AI-driven compression
Booking simulation engine

🔐 Security Considerations
API key stored using environment variable
Model stored locally via pickle
No sensitive user data stored

🔮 Future Scope
Trainer-based recommendation
Rating-based filtering
Real-time booking database
Attendance analytics dashboard
Membership renewal automation
Hybrid recommendation (content + collaborative filtering)

🎓 Academic Contribution
This project demonstrates:
Integration of ML and GenAI
Real-world system simulation
Feature engineering and preprocessing
Model deployment in interactive UI
Scalable system architecture design

📌 Key Takeaways
Lightweight ML can power personalization effectively.
GenAI can optimize textual data for improved UX.
Clean architecture allows future scalability.
AI systems should be modular and expandable.
