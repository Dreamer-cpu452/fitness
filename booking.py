import pandas as pd

# Load compressed class data
classes_df = pd.read_csv("classes_compressed.csv")

# Initialize booking and waitlist tracking
bookings = {}
waitlists = {}

# Initialize structures
for _, row in classes_df.iterrows():
    class_name = row["class_name"]
    bookings[class_name] = []
    waitlists[class_name] = []

def book_class(user_id, class_name):
    capacity = classes_df[classes_df["class_name"] == class_name]["capacity"].values[0]

    if len(bookings[class_name]) < capacity:
        bookings[class_name].append(user_id)
        return f"User {user_id} successfully booked {class_name}"
    else:
        waitlists[class_name].append(user_id)
        return f"Class full. User {user_id} added to waitlist."

def cancel_booking(user_id, class_name):
    if user_id in bookings[class_name]:
        bookings[class_name].remove(user_id)

        # Promote from waitlist if exists
        if waitlists[class_name]:
            promoted_user = waitlists[class_name].pop(0)
            bookings[class_name].append(promoted_user)
            return f"User {user_id} cancelled. User {promoted_user} promoted from waitlist."
        return f"User {user_id} booking cancelled."

    return "User not found in booking list."

# Example testing
print(book_class(101, "HIIT"))
print(book_class(102, "HIIT"))
print(cancel_booking(101, "HIIT"))
