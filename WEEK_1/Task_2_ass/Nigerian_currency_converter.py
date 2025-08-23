# file 11

# Nigerian Currency Converter (Very Adavnced)

# naira conversion to us dollar
us_dollar_rate=(0.00065) # 1 naira  to us dollar is 0.00065
amount_in_naira =float(input("ENTER NAIRA AMOUNT YOU WANT TO CONVERT TO US DOLLAR: ")) # user enter naira amount they want to convert to dollar

# naira convesion to british pounds 
br_pounds_rate =(0.00049) # 1 naira to british pounds is 0.00049
amount_in_naira1 =float(input("ENTER NAIRA AMOUNT YOU WANT TO CONVERT TO BRITISH POUNDS: ")) # user enter naira amount they want to convert to pounds

# neatly aligned in a table-like using escape sequnce
print("\n\t NIGERIA CURRENCY CONVERSION TABLE")
print("\t_________________________________________")
print(f"\n\tNAIRA RATE\tDOLLAR RATE")
print(f"\t₦{amount_in_naira}\t\t${amount_in_naira * us_dollar_rate:.2f}")
print(f"\n\tNAIRA RATE\tPOUNDS RATE")
print(f"\t₦{amount_in_naira1}\t\t£{amount_in_naira1 * br_pounds_rate:.2f}")
print("\t_________________________________________")
