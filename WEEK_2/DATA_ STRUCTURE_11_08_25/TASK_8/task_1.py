# Task1
# Explain each output of the program below

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# # Output: 4 == 5 : False # The reason the output result is False is that (num1) is not equal to (num2) example (4  == 5)

print(f"{num1} != {num2} : {num1 != num2}")
# Output: 4 != 5: True # The reason the output is True is that (4 is not equal to 5) which the correct operators indicate

print(f"{num1} > {num2} : {num1 > num2}")
# Output: 4 > 5 : False # The reason the output is False is that (4 is not greater than 5 )

print(f"{num1} < {num2} : {num1 < num2 }")
# Ouput: 4 < 5: True # The reason the output is True is that (4 is less than 5)

# # Give 3 usescases or scenarios where you can apply the program 
# # Student Exam Result
# # To check Age Eligibility
# # To cut-off mark

#  Write a code for age eligibility
print("To proceed to this scholarship program we need to confirm your age")
user_input = int(input("Enter your age: "))
age = 20 # Defined variable

eligibility = (user_input < 20)
print(f"Your are eligible to proceed", {eligibility})

