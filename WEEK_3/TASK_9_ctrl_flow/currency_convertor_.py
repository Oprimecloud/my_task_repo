# Nigerian Currency Converter (Very Adavnced)
# Using "IF" AND "ELSE"
# naira conversion to us dollar
us_dollar_rate=(0.00065) # 1 naira  to us dollar is 0.00065
amount_in_naira =float(input("Enter naira amount you want to convert to dollar: ")) # user enter naira amount they want to convert to dollar

# naira convesion to british pounds 
br_pounds_rate =(0.00049) # 1 naira to british pounds is 0.00049
amount_in_naira1 =float(input("Enter naira amount you want to convert to british pounds: ")) # user enter naira amount they want to convert to pounds

if amount_in_naira <= 0 or amount_in_naira1 <= 0:
    print("Exchange rates must be greater than zero!")
else:
    # conversion
   usd = amount_in_naira * us_dollar_rate
   gbp = amount_in_naira1 * br_pounds_rate

# neatly aligned in a table-like using escape sequnce
print("\n\t NIGERIA CURRENCY CONVERSION TABLE")
print("\t_________________________________________")
print(f"\n\tNAIRA RATE\tDOLLAR RATE")
print(f"\t₦{amount_in_naira}\t\t${usd:.2f}")
print(f"\n\tNAIRA RATE\tPOUNDS RATE")
print(f"\t₦{amount_in_naira1}\t\t£{gbp:.2f}")
print("\t_________________________________________")