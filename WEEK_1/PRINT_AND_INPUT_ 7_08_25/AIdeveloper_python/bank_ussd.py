# step 1 creating a welcome message with option menu
# step 2 creating menu for each options

# defind ussd
def ussd_menu():
    while True:   #bool statement
        print("\nWelcome to Optimist Bank")
        print("1. Check Balnace")
        print("2. Transfer")
        print("3. Buy Airtime")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            print("\nYour account balance is $30,000.00")
        
        elif choice == "2":
            transfer_menu()

        elif choice == "3":
            airtime_menu()

        elif choice == "4":
            print("Thank you for using optimist Bank.")
            break

        else:
            print("invalid input. Please try again.")

def transfer_menu():
        print("\nTransfer Money:")
        print("1. To optimist Bank")
        print("2. To other Banks")
        print("3. Back")

        option = input("choose an option: ")

        if option in ["1", "2"]:
            account_number = input("Enter recipient's account number: ")
            account_name = input("Enter account name: ")
            amount = input("Enter amount to transfer: ")
            if option == "2":
                print("\nselect bank:")
                print("1. GTBank")
                print("2. Access Bank")
                print("3. Opay Bank")
                print("4. Kuda Bank")
                bank_choice = input("choose Bank: ")
            print("\nConfirm Transfer:")
            print(f"Account Number: {account_number}")
            print(f"Account Name: {account_name}")
            print(f"Amount: ${amount}")
            confirm = input("Enter 1 to Confirm or 2 to Cancel: ")
            if confirm == "1":
                pin = input("Enter your 4-digit PIN: ")
                print(f"\nTransferring ${amount} to {account_name}")
                print("Transfer successful! Thank you.")
            else:
                    print("Transfer cancelled.")

        elif option == "3":
            return
            
        else:
            print("Invalid option.")


def airtime_menu():
        print("\nBuy Airtime:")
        print("1. self")
        print("2. others")
        print("3. Back")

        option = input("Choose an option: ")

        if option == "1":
            amount = input("Enter amount: ")
            print(f"Airtime of ${amount} recharged successfully to your line.")
        elif option == "2":
            phone = input("Enter recipient's phone number: " )
            amount = input("Enter amount: ")
            print(f"Airtime of ${amount} recharged sucessfully to {phone}.")
        elif option == "3":
            return
        else:
            print("Invalid option.")


ussd_menu()
