import os

if os.path.exists("classes_compressed.csv"):
    print("Compressed file already exists. Skipping API calls.")
    exit()

from google import genai
import pandas as pd
import time

import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def compress_text(text):
    prompt = f"""
    Compress the following gym class description into one short, clear sentence 
    while preserving the main fitness objective:

    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
    )

    return response.text.strip()

# Load dataset
classes_df = pd.read_csv("classes.csv")

print("\n--- GEMINI CLASS DESCRIPTION COMPRESSION ---\n")

compressed_list = []
response_times = []

for index, row in classes_df.iterrows():
    original = row["description"]

    start_time = time.time()
    compressed = compress_text(original)
    end_time = time.time()

    compressed_list.append(compressed)
    response_times.append(round(end_time - start_time, 2))

    print("Class:", row["class_name"])
    print("Original Length:", len(original))
    print("Compressed Length:", len(compressed))
    print("Compressed Text:", compressed)
    print("Response Time (seconds):", round(end_time - start_time, 2))
    print("-" * 60)

# Add compressed column
classes_df["compressed_description"] = compressed_list
classes_df["response_time"] = response_times

# Save new CSV
classes_df.to_csv("classes_compressed.csv", index=False)

print("\nCompressed dataset saved successfully!")

# ---------------- TRAINER PROFILE COMPRESSION ----------------

trainers_df = pd.read_csv("trainers.csv")

print("\n--- GEMINI TRAINER PROFILE COMPRESSION ---\n")

trainer_compressed_list = []

for index, row in trainers_df.iterrows():
    original_profile = row["profile_description"]

    compressed_profile = compress_text(original_profile)
    trainer_compressed_list.append(compressed_profile)

    print("Trainer:", row["trainer_name"])
    print("Original Length:", len(original_profile))
    print("Compressed Length:", len(compressed_profile))
    print("Compressed Text:", compressed_profile)
    print("-" * 60)

trainers_df["compressed_profile"] = trainer_compressed_list
trainers_df.to_csv("trainers_compressed.csv", index=False)

print("\nTrainer dataset saved successfully!")
