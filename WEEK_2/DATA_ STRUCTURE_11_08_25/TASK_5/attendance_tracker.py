# Task 6 Attendance Tracker
# write a python program that; 
# stores the days of the week in a tuple.
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# store the months of the year in another tuple.
months_of_the_year = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# input
# Asks the user to enter:
student_name = input("Enter your name: ")
gender = input("What's your gender: ")
course_track =input("What's your course track: ")
current_month_number =int(input("Enter current month number from (1-12): "))
current_day_number  =int(input("Enter current day number from (1-7): "))
profile = student_name , gender, course_track, current_month_number, current_day_number
print(profile)
