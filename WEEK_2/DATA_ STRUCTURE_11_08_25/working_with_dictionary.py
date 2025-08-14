#  python Dictionaries
# A dictionary in python is a collection of key-value pairs.
# values can be any data type(string, integer, list, tuple, even nother dictionary)

# syntax
# dictionary_name = {Key1: value1, Key2: value2}

# Characteristics of dictionaries
# 1. Key-value structure: Each item is stored as a key: value pair.

# 2. **Mutable**: You can add, change, or remove items.

# 3. **Unordered (before Python 3.7)**:  From Python 3.7+, they maintain insertion order.

# 4. **Unique Keys**:  No duplicate keys allowed; a new assignment to an existing key overwrites the old value.

# 5. **Keys must be immutable**:  Strings, numbers, tuples (containing only immutable items) can be keys.

# Creating Dictionaries

# 1.Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer science"
}
print(student)


#  2. Using the dict() constructor
student_info = dict(name="john", age="25", course="Maths")
print(student_info)

# 3. Empty dictionary
empty_dict = {}
print(empty_dict)

# How to add  key-value pairs to an empty dictionary
# Create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)

# 4 Dictionary Comphrension
# Syntax:
# {Key_expression: Value_expression for item in iterable if condition}

# create a dictionary of numers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# with condition

# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0} # to print even_cubs you have == 0
odds_cube = {x: x**3 for x in range(1, 10) if x % 2 != 0} # to print odds cube you have to use != 0
print(evens_cube)
print(odds_cube)

# from Existing Dictionary 
students = {"Ada": 85, "john": 40, "Musa": 65}

# Filter students who passed (score >= 50)

passed_students = {name: score for name, score in students.items() if score>= 50 }
print(passed_students)

# Using String Keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Accessing Dictionary Items

# Define a dictionary
student = {
    "name": "Ada", 
    "age": 20,
    # "grade": 2,
    "course": "Computer Science"
}

# Using key
print(student["name"])

# Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "Not Found"))

# Modifying Dictionaries
student["age"] = 21 # change value
student["grade"] = "A" # Add newe key-value pair
print(student)

# Removing items from dictionaries
# 1. Using pop()
student.pop("grade")

#2. Using popitem() - removes last inserted key-value
student.popitem()

# 3. Using del keyword
del student["age"]

# 4. Using clear() - removes all items
student.clear()

print(student)

# Dictionary methods

# dot keys(), dor values(), dot items(), dot update()

person = {"name": "Emeka", "age": 30}

# 1. Keys()
print(person.keys())

# 2. values()
print(person.values())

#3. items()
print(person.items())

# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)

# Nested Dictionaries
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}
print(students["student1"]["name"])  # Access nested data

# Looping Through Dictionaries

# Define a dictionary
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# storing a student's biodata
student = {
    "name": "Chinedu",
    "age:": 19,
    "department": "Development",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")

# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])   
print(students[1]["Track"])  

# Dictionary of dictionaries - Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1])