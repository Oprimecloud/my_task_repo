# Basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to integer
age = int(input("Enter your age:"))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

# step 1 create a welcome message
# step 2 create a input to request order

# Greetings
greeting = "Hello welcome to optimist bar"
print(greeting)

# order
order = input("what drink will you like to order:")
print("You ordered:", order)

# confirmation
confirm = input("pls kindly confirm your order by proceed: ")
print("Thanks for the patronage")


#welcome message
welcome = "welcome to optimist !"
print(welcome)

#what do you want to do
list = input("kindly press type enter:")
print("choose option")
list = ("1. bank transfer\n2. check balance \n3. withdraw \n4. deposit")
print(list)

#select option
bank_acc = input("press 1 to transfer:")
bank_acc = input("enter destination account number:")
print(bank_acc)
