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
print("\n|-------------------------------")
print(f"| Basic Calculator Program") #Welcome message

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
            print("|============+++++=============")
            print("|Select Operation:")
            print("|1. Addition")
            print("|2. Subtraction")
            print("|3. Multiplication")
            print("|4. Division")
            print("|5. Exponentiation")
            print("|6. Square Root")
            print("|7. Exit")
            print("|============++++++==============")

# Take input from the user for operation choice
            choice = int(input(" Enter Option from 1 - 7): "))
            if choice in range(1,6):
# Get two numbers asinput from the usee
                print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
                num1 = float(input("  Enter first number: "))
                num2 = float(input("  Enter second number: "))
                print("|~~~~~~~~~~~~~~~~~~~~~~~~|")

# Perform calulation based on user,s choice
                if choice == 1:
                    print("  ><><><><><><><><><><>")
                    print("  Results:", add(num1, num2))
                    print("  ><><><><><><><><><><>")
                elif choice == 2:
                    print("  ><><><><><><><><><><>")
                    print("Results:", subtract(num1, num2))
                    print("  ><><><><><><><><><><>")
                elif choice == 3:
                    print("  ><><><><><><><><><><>")
                    print("Results:", multiply(num1, num2))
                    print("  ><><><><><><><><><><>")
                elif choice == 4:
                    print("  ><><><><><><><><><><>")
                    print("Result:", divide(num1, num2))
                    print("  ><><><><><><><><><><>")
                elif choice == 5:
                    print("  ><><><><><><><><><><>")
                    print("Results:", exp(num1, num2))
                    print("  ><><><><><><><><><><>")
            
            elif choice == 6:
                print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
                num1 = float(input(" Enter number: "))
                print("|~~~~~~~~~~~~~~~~~~~~~~~~|")
                if num1 < 0:
                    print("Error: cannot calculate square root of a negative number.")
                else:
                    result = math.sqrt(num1)
                    print("  ><><><><><><><><><><>")
                    print("Result:",result)
                    print("  ><><><><><><><><><><>")
            elif choice == 7:
                print("Shutting calculator down.. 😃")
                break
            else:
                print("Invalid Option👺, enter a valid option from above")
        except ValueError as e:
            print("Error: ", e)
main()



