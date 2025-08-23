# file 12 

# simulated ussd 
# print welcome message 
print("WELCOME TO JUJU BANK")

# ask user dial *123#
dail =str(input("KINDLY DAIL A USSD CODE (e.g., *123#): "))

# print a menu option
print("\nMain Menu\n1. Check Balance\n2. Buy Airtime\n3. Buy Airtime") 

# Ask for option (1,2, or 3)
choice =int(input("please select an option(1, 2, or 3): "))

# use f-strings to display the option selected
print(f"you selected option {choice}")

# if applicable, ask amount
amount = float(input("Enter amount in Naira: "))
print(f"₦{amount:.2f}")

# Final message 
print("Thanks for banking with us!!!")





