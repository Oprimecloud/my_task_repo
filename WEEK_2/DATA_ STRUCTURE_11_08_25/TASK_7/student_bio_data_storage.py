# Student Bio Data Storage
#  Create a program that collects student bio-data from the user input 
# (name, age, gender, course) and stores it in a dictionary.
# course shoudle be stored as a list
# Display the bio-data neatly using escape sequences

# collect user input
name = input("Kindly enter your name: ")
age = int(input("How old are you: "))
gender = input("What is your gender: ")
courses = input("Enter your courses you are studying(separated by commas): ")

# store user input in dictionary
student_biodata = {}
student_biodata["Name"] = name
student_biodata["Age"] = age
student_biodata["Gender"] = gender
student_biodata["Courses"] = courses.split(",") # Cousres should be stored as list
print((student_biodata))

# Display the bio-data neatly using escape sequences.
print("\n---STUDENT BIO DATA---")
print(f"Name:\t {student_biodata['Name']}")
print(f"Age:\t {student_biodata['Age']}")
print(f"Gender:\t {student_biodata['Gender']}")
print(f"Courses:\t{student_biodata['Courses']}")
