def ussd_menu():
    while True:
        print("\nWelcome to XYZ Bank")
        print("1. Check Balance")
        print("2. Transfer")
        print("3. Buy Airtime")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print("\nYour account balance is ₦25,000.00")

        elif choice == "2":
            transfer_menu()

        elif choice == "3":
            airtime_menu()

        elif choice == "4":
            print("Thank you for using XYZ Bank.")
            break

        else:
            print("Invalid input. Please try again.")


def transfer_menu():
    print("\nTransfer Money:")
    print("1. To XYZ Bank")
    print("2. To Other Banks")
    print("3. Back")

    option = input("Choose an option: ")

    if option in ["1", "2"]:
        account_number = input("Enter recipient's account number: ")
        amount = input("Enter amount to transfer: ")
        if option == "2":
            print("\nSelect bank:")
            print("1. First Bank")
            print("2. GTBank")
            print("3. Access Bank")
            print("4. UBA")
            bank_choice = input("Choose bank: ")
        print("\nConfirm Transfer:")
        print(f"Account: {account_number}")
        print(f"Amount: ₦{amount}")
        confirm = input("Enter 1 to Confirm or 2 to Cancel: ")
        if confirm == "1":
            pin = input("Enter your 4-digit PIN: ")
            print("Transfer successful! Thank you.")
        else:
            print("Transfer cancelled.")

    elif option == "3":
        return

    else:
        print("Invalid option.")


def airtime_menu():
    print("\nBuy Airtime:")
    print("1. Self")
    print("2. Others")
    print("3. Back")

    option = input("Choose an option: ")

    if option == "1":
        amount = input("Enter amount: ")
        print(f"Airtime of ₦{amount} recharged successfully to your line.")
    elif option == "2":
        phone = input("Enter recipient's phone number: ")
        amount = input("Enter amount: ")
        print(f"Airtime of ₦{amount} recharged successfully to {phone}.")
    elif option == "3":
        return
    else:
        print("Invalid option.")


# Run the USSD simulation
ussd_menu()
