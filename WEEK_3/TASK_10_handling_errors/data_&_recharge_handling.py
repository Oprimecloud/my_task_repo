# create a ussd recharge code
# using while true

# Ussd Code
code = "*234#"

while True:
    try:
        Dail = input("Dial *234#: ").title()
        if Dail == code:
            print("\nWelcome to jaja Network Service Bot!")
            break
        else:
            print("Invalid code, Dial *234#")
    except Exception as e:
        print(f"An error occurred: {e}")

Balance = 1000

try:
    print("Select your option:")
    print("1. Airtime")
    print("2. Data")
    print("3. Exit")

    choose = input("Select Option: ")

    if choose == "1":
        print("You selected Airtime:")
        print("Select or Enter Amount(Min N50.0)\n1. 50\n2. 100\n3. 200\n4. 300\n4. 400\n5. 500\n6. 1000")

        try:
            Amount = int(input("Enter Amount: "))
            if Amount <= Balance:
                Balance -= Amount
                enter_number = input("Enter destination number: ")
                print(f"You have successfully recharged N{Amount} to this number {enter_number}")
                print(f"Your New balance is: N{Balance}")
            else:
                print("Insufficient Balance, Try small amount")
        except ValueError:
            print("Error: Please enter a valid amount.")

    elif choose == "2":
        print("\nYou selected Data:")
        print("Select Data Plan:\n1. 500MB - N750\n2. 1.5GB - N1500\n3. 3GB - N2500\n4. 10GB - N5000")
        data_plan = input("Select data plan: ")

        if data_plan in ["1", "2", "3", "4"]:
            num = input("Enter recipient number: ")
            plans = {
                "1": "500MB",
                "2": "1.5GB",
                "3": "3GB",
                "4": "10GB"
            }
            print(f"You have successfully purchased {plans[data_plan]} data to this number {num}")
        else:
            print("Invalid entry, Select from the option above")

    elif choose == "3":
        print("Thanks for using Jaja Network Service.")

    else:
        print("Invalid Option! Try again")

except Exception as e:
    print(f"An unexpected error occurred: {e}")