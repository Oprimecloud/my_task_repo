#  A basic calculator is one of the fundamental
# projects in Python programming. It provides essential
# arithmetic operations such as addition, subtraction,
# multiplication, and division. Understanding how to
# implement a calculator helps in learning user input
# handling, conditional statements, and function creation in
# Python.

# # Key Concepts of Basic Calculator in Python
#  Arithmetic Operations:
#  Addition ( + )
#  Subtraction (- )
#  Multiplication ( * )
#  Division ( / )
#  Modulus ( % )
#  Exponentiation ( ** )
#  User Input Handling:
#  Using input() function
#  Converting strings to integers or floats
#  Functions in Python:
#  Defining functions for calculations
#  Calling functions with user inputs
#  Error Handling:
#  Parameter Table
#  Operator
#  Handling division by zero
#  Handling invalid inputs

import math  # import math module for square root function
print(f"\nBasic Calculator Program") #Welcome message

# Function added (addition, subtraction, multiplication, division, exponentiation)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return(a * b)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def exp(a, b):
    return a ** b

# Display operation options to the user
def main():
    while True:
        try: # Function for error handling, input validation
            print("\nSelect Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Square Root")
            print("7. Exit")

# Take input from the user for operation choice
            choice = int(input("Enter Option (1 or 2 or 3 or 4 or 5 or 6 or 7): "))
            if choice in range(1,6):
# Get two numbers asinput from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

# Perform calulation based on user,s choice
                if choice == 1:
                    print("Results:", add(num1, num2))
                elif choice == 2:
                    print("Results:", subtract(num1, num2))
                elif choice == 3:
                    print("Results:", multiply(num1, num2))
                elif choice == 4:
                    print("Result:", divide(num1, num2))
                elif choice == 5:
                    print("Results:", exp(num1, num2))
            
            elif choice == 6:
                num1 = float(input("Enter number: "))
                if num1 < 0:
                    print("Error: cannot calculate square root of a negative number.")
                else:
                    result = math.sqrt(num1)
                    print("Result:",result)
            elif choice == 7:
                print("Shutting calculator down.. 😃")
                break
            else:
                print("Invalid Option👺, enter a valid option from above")
        except ValueError as e:
            print("Error: ", e)
main()



