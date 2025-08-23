# create a ussd recharge code
# using while true
# Ussd Code
code = "*234#"
while True:
    Dail = input("Dial *234#:").title()
    if Dail == code:
        print("\nWelcome to jaja Network Service Bot!")
        break
    else:
         print("Invalid code, Dial*234#")
Balance = 1000
print("Select your option:")
print("1. Airtime")
print("2. Data")
print("3. Exit")
choose = input("Select Option:")
if choose == "1":
    print("You selected Airtime:")
    print("Select or Enter Amount(Min N50.0)\n1. 50\n2. 100\n3. 200\n4. 300\n4. 400\n5. 500\n6. 1000")
    Amount = int(input("Enter Amount: "))
    if Amount <= Balance:
        Balance -= Amount
        enter_number = input("Enter destination number: ")
        print(f"You have successful recharged N{Amount} to this number {enter_number}")
        print(f"Your New balance is:N{Balance}")
    else:
        print("Insufficient Balance, Try small amount")
elif choose == "2":
    print("\nYou selected Data:")
    print("Select Data Plan:\n1. 500MB - N750\n2. 1.5GB - N1500\n3. 3GB -   N2500\n4. 10GB -  N5000")
    data_plan = (input("Select data plan:"))
    if data_plan == "1":
        num = input("Enter recipient number:")
        print(f"You have successfully purchased 500MB data to this number {num}")
    elif data_plan == "2":
        num = input("Enter recipient number:")
        print(f"You have successfully purchased 1.5GB data to this number {num}")
    elif data_plan == "3":
        num = input("Enter recipient number:")
        print(f"You have successfully purchased 3GB data to this number {num}")
    elif data_plan == "4":
        num = input("Enter recipient number:")
        print(f"You have successfully purchased 10GB data to this number {num}")
    else:
        print("Invalid entry, Select from the option above")
elif choose == "3":
    print("Thanks for using Jaja Network Service.")
else:
    print("Invalid Option! Try again")
