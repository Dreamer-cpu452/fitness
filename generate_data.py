import pandas as pd
import numpy as np
import random

# ---------------- USERS DATA ----------------
num_users = 500

fitness_goals = ["Weight Loss", "Muscle Gain", "Flexibility"]
experience_levels = ["Beginner", "Intermediate", "Advanced"]
preferred_times = ["Morning", "Evening"]
genders = ["Male", "Female"]

def assign_class(goal):
    if goal == "Weight Loss":
        return random.choice(["HIIT", "Cardio Blast", "Zumba"])
    elif goal == "Muscle Gain":
        return random.choice(["Strength Training", "CrossFit"])
    else:
        return random.choice(["Yoga", "Pilates"])

users = []

for i in range(1, num_users + 1):
    goal = random.choice(fitness_goals)
    users.append({
        "user_id": i,
        "age": random.randint(18, 50),
        "gender": random.choice(genders),
        "bmi": round(random.uniform(18, 32), 1),
        "fitness_goal": goal,
        "experience_level": random.choice(experience_levels),
        "weekly_attendance": random.randint(0, 5),
        "preferred_time": random.choice(preferred_times),
        "recommended_class": assign_class(goal)
    })

users_df = pd.DataFrame(users)
users_df.to_csv("users.csv", index=False)

# ---------------- CLASSES DATA ----------------
classes = [
    {
        "class_id": 1,
        "class_name": "HIIT",
        "duration": 45,
        "intensity": "High",
        "trainer_name": "Rahul",
        "capacity": 20,
        "description": "High intensity interval training session focusing on fat burn and stamina improvement."
    },
    {
        "class_id": 2,
        "class_name": "Cardio Blast",
        "duration": 40,
        "intensity": "High",
        "trainer_name": "Rahul",
        "capacity": 20,
        "description": "Energetic cardio workout designed to improve heart health and calorie burning."
    },
    {
        "class_id": 3,
        "class_name": "Zumba",
        "duration": 50,
        "intensity": "Medium",
        "trainer_name": "Anjali",
        "capacity": 25,
        "description": "Dance-based fitness program combining Latin rhythms with calorie-burning moves."
    },
    {
        "class_id": 4,
        "class_name": "Strength Training",
        "duration": 50,
        "intensity": "Medium",
        "trainer_name": "Vikram",
        "capacity": 18,
        "description": "Resistance-based training to build muscle mass and endurance."
    },
    {
        "class_id": 5,
        "class_name": "CrossFit",
        "duration": 60,
        "intensity": "High",
        "trainer_name": "Vikram",
        "capacity": 15,
        "description": "Functional fitness training combining strength and conditioning movements."
    },
    {
        "class_id": 6,
        "class_name": "Yoga",
        "duration": 60,
        "intensity": "Low",
        "trainer_name": "Anjali",
        "capacity": 25,
        "description": "Guided yoga session to improve flexibility and reduce stress."
    },
    {
        "class_id": 7,
        "class_name": "Pilates",
        "duration": 45,
        "intensity": "Low",
        "trainer_name": "Anjali",
        "capacity": 20,
        "description": "Core-focused workout designed to improve posture and stability."
    }
]

classes_df = pd.DataFrame(classes)
classes_df.to_csv("classes.csv", index=False)

# ---------------- TRAINERS DATA ----------------
trainers = [
    {
        "trainer_id": 1,
        "trainer_name": "Rahul",
        "specialization": "HIIT",
        "experience_years": 5,
        "rating": 4.6,
        "profile_description": "Certified HIIT specialist with experience in athletic conditioning and high-performance training."
    },
    {
        "trainer_id": 2,
        "trainer_name": "Anjali",
        "specialization": "Yoga",
        "experience_years": 7,
        "rating": 4.8,
        "profile_description": "Professional yoga instructor specializing in flexibility, mindfulness, and stress reduction techniques."
    }
]

trainers_df = pd.DataFrame(trainers)
trainers_df.to_csv("trainers.csv", index=False)

print("Datasets generated successfully!")
