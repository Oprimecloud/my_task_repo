# file 6

# asking for data
customer_full_name =input("ENTER YOUR FULL NAME: ")
units_consumed =int(input("ENTER YOUR UNITS: "))
cost_per_unit =float(input("ENTER PRICE PER UNITS: "))
total_bill = (units_consumed * cost_per_unit)
print("\t\t\tTHIS IS YOUR BILL") #just adding to make it stylish
print("\t----------------------------------------------------------") # just adding to make it stylish
print(f"\tCUSTOMER NAME\tUNIT CONSUMED\tCOST PER UNIT\tTOTAL BILL\n\t{customer_full_name}\t{units_consumed} kWh\t\t₦{cost_per_unit}\t\t₦{total_bill}K") # main code to print the bill format using escape sequnces for line breaks
print("\t----------------------------------------------------------") # just addding to make it stylish


