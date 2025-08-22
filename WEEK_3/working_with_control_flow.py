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
    print(char) # to prevent the  string to be in a new each you can use end=""

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

# - You are building continuous programs like menus, login systems, or stimulations.

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

#  2. Continue

# - Skips the current iteration and moves to the next one. It is used if you want to ignore some values but keep the loop running.

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 3 is skipped, but the loop continues.

## Some usecases

#Skip invalid data.

#Ignore unwanted characters (like spaces in a string).

#Continue running but avoid certain cases, etc.

# 3. Pass

# - Does nothing. A placeholder to avoid errors. It is used If you haven’t written the code yet but want to keep the structure.

for num in range(1, 6):
    if num == 3:
        pass   # do nothing for now
    else:
        print(num)

# At num == 3, Python executes pass (nothing happens).

## Some usecases

# Writing code structure (to fill in later).

# Placeholders in class/method definitions.

# Temporarily disable parts of code.

# Lets try while True again
# Try and think through this...

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

# Menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit

# Try and use while True for validation

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# LEets make a guess

secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")

# Do you remember this?

balance = 1000  

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":  
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

