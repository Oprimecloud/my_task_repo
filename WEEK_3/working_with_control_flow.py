# Control Flow in python
# Control flow refers to the order in which statements are executed in a program.
# Instead of always running line by line, control flow allows your program to:

#     - Make decisions (choose one path or another, explore alternatives).
#     - Repeat actions (loops).
#     - Exit or skip parts of code.

# - It is the foundation for logic and problem solving in programming.
# - Control flow is divided into 3 parts

# A. Conditional Statements

# 1. if statement
# executes a block only when a condition is true.

age = 20
if age >= 18:
    print("You are eligible to vote")
# Output: You are eligible to vote

# Some usecase
# Checking for eligibility.
# Validating Login attempts
# Ensuring a minimum purchase requirements, etc

# 2. if-else Statment
# provides two alternative paths.

wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")
# Output: Insufficient balance

# Some usecases
# Deciding success or failure of a payment.
# Granting or denying access to a system.
# Determing pass/fail in an exam, etc.
 
# 3. If-elif-else Statement
# used for multiple conditions.
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")
# Output : Grade A

# Some usecases**
# - Student grading systems.
# - Assigning ticket categories (VIP, Regular, Student).
# - Categorizing temperatures (Hot, Warm, Cold), etc.

# Nested if
# palcing an if inside another if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

# Output: You can vote

# Some usecases**
# - Voting eligibility (age + citizenship).
# - Banking (account active + balance sufficient).
# - School admission (age + grade level).

# B. Loops

# 1. for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)

# Iterates through each element in a LIST.

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Some usecases
# Iterating through shopping lists.
# Checking availability of products.
# Displaying student names, etc.

# Ouput: I like apple
#        I like banana
#        I like orange

# Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

## Some usecases
# Storing fixed sensor readings.
# Displaying fixed seating positions, etc.
# Ouput: Point: 0.34654
#        Point: -0.48585
#        Point: 0.57477

# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
## Some usecases
# Reading database records.
# Showing user profile details.
# Checking configuration settings, etc.

# Output: name: Tunde
#         age: 16
#         grade: A

# Iterates through each element in a STRING. Remember that strings are sequences of characters.

word = "PYTHON"
for char in word:
    print(char)

## Some usecases
# Counting vowels/consonants.
# Password validation (checking digits/special chars).
# Text analysis, etc.

# 2. While loop
# A while loop is used to repeatedly execute a block of code **as long as a given condition is true.**
# Unlike the for loop (which iterates over sequences like lists, tuples, etc.), the while loop is condition-based.

# ```
# while condition:
#     # code block
# ```
# - The condition must evaluate to `True` for the loop to continue running.
# - When the condition becomes `False`, the loop stops.

# Using while loop

## Documenting my thoughts##
# Let the loop start with count = 1
# Let it keep printing until count is greater than 5
# Let the loop terminate when the condition is no longer true

## My code
count = 1
while count <= 5:
    print("Number:", count)
    count +=1
# Output :  Number: 1
            # Number: 2
            # Number: 3
            # Number: 4
            # Number: 5

# Incrementing with 'while'

num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
# Output = 1 2 3 4 5 6 7 8 9 10 

# Decrementing with 'while'
timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1
# # Countdown: 10
# Countdown: 9
# Countdown: 8
# Countdown: 7
# Countdown: 6
# Countdown: 5
# Countdown: 4
# Countdown: 3
# Countdown: 2
# Countdown: 1

# While with User Input
## Keep asking until the user enters a correct password.

password = ""
while password != "Python123":
    password = input("Enter the password: ")

print("Access Granted!")

# Understanding `while True`**

# - The while True: loop is an infinite loop — it keeps running forever until you explicitly stop it with a break statement or by exiting the program.

# - It is commonly used when:

# - You don’t know in advance how many times you want the loop to run.

# - You want to keep asking the user for input until a valid condition is met.

# - You are building continuous programs like menus, login systems, or simulations.

# ```
# while True:
#     # Code block
#     # Must include a break statement to stop

# Keep asking the user for a name until they type "exit".

while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")
    
# ---> I used `break` here. If you dont know what it is or what it is doing, its OK. I will explain it next...
## Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.

# Loop Control Statements (`break`, `continue` and `pass`)
# These keywords help us control the behavior of loops (for and while). Instead of loops always running all iterations, we can skip steps, stop early, or do nothing intentionally.

# 1.  break
# Stops loop immediately. It is used if a condition is met and there’s no need to continue looping.

for num in range(1, 10):
    if num == 5:
        break
    print(num)
#The loop stops completely when num == 5.

# Stop searching when an item is found.

# Exit when user input matches a condition.

# Prevent unnecessary iterations.