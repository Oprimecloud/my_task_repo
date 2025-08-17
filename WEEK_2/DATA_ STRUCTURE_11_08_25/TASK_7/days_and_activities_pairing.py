# Days and Activities Pairing
# Store Days of the week in a tuple and ask the user to input an activity for three specific days.
# Days of the week stored in a tuple
days_of_the_weeks = ("Sunday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday")

# Ask user to input activity for three specific days
activity_day1=input("Enter activity done: ")
activity_day2=input("Enter activity done: ")
activity_day3=input("Enter activity done: ")

# collect activities in a list to stop overwriting 
activities = [activity_day1, activity_day2, activity_day3]

# Pair each activity to a specified day using zip
specific_day = [days_of_the_weeks[0], days_of_the_weeks[1], days_of_the_weeks[2]]

day_activity = zip(specific_day, activities)
print(f"Days and Activities:", dict(day_activity))