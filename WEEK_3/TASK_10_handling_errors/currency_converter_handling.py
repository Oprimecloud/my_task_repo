# Nigerian Currency Converter (Very Advanced)
# Using "IF" AND "ELSE"

us_dollar_rate = (0.00065)  # 1 naira to US dollar
br_pounds_rate = (0.00049)  # 1 naira to British pounds

try:
    # Get user input for Naira to Dollar
    amount_in_naira = float(input("Enter naira amount you want to convert to dollar: "))
    
    # Get user input for Naira to Pounds
    amount_in_naira1 = float(input("Enter naira amount you want to convert to british pounds: "))

    # Validate inputs
    if amount_in_naira <= 0 or amount_in_naira1 <= 0:
        print("Exchange amounts must be greater than zero!")
    else:
        # Conversion
        usd = amount_in_naira * us_dollar_rate
        gbp = amount_in_naira1 * br_pounds_rate

        # Display results in a table format
        print("\n\t NIGERIA CURRENCY CONVERSION TABLE")
        print("\t_________________________________________")
        print(f"\n\tNAIRA RATE\tDOLLAR RATE")
        print(f"\t₦{amount_in_naira:,.2f}\t\t${usd:,.2f}")
        print(f"\n\tNAIRA RATE\tPOUNDS RATE")
        print(f"\t₦{amount_in_naira1:,.2f}\t\t£{gbp:,.2f}")
        print("\t_________________________________________")

except ValueError:
    print("Error: Please enter a valid numeric value for the amount.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")