# Creating a bank ussd for koko bank
# Get started 
secret = "*420#"

while True:
    start = input("Dail *420# to get started: ").title()
    if start == secret:
         print("Welcome to koko bank!!!")
         break
    else:
         print("Wrong code! Dial *420#.")

balance = 50000
while True:
    print("\nMain Menu:") # welcome message 
    print("1. Check Balance")
    print("2. Bank Transfer")
    print("0. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        print(f"Your balance is: ₦{balance}")
        continue

    elif choice == "2":
        print("\nTransfer Menu: ")
        print("1. Koko Bank")
        print("2. Kuda Bank")
        print("3. Jaiz Bank")
        print("0. Exit")
    elif choice == "0":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid option. Try again.")
        continue

    option = input("Enter Your Option: ")
        
    if option in ["1", "2", "3"]:
        try:
            account_number = input("Enter recipient's account number: ")
            account_name = input("Enter account name: ")
            
            # Error handling for amount input
            amount = int(input("Enter amount to transfer: "))
            
            if amount <= balance:
                balance -= amount
                print(f"₦{amount} was successfully transferred to {account_name}. \nNew balance: ₦{balance}")
            else:
                print("Insufficient funds.")
        
        except ValueError:
            print("Error: Please enter a valid number for amount.")
            continue

    elif option == "0":
        print(f"Thank you for banking with us.")
        break
    else:
        print("Invalid Option. Try again.")
    
