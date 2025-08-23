# file 5

# Daily market report ask the user to input
market_name = input("Enter market name: ")
number_of_traders = int(input("Enter number of trader: "))
daily_revenue_in_naira = float(input("Enter daily revenue: "))

print(f"\nDaily Market Report for{market_name}\n{market_name} has {number_of_traders} traders with ₦{daily_revenue_in_naira}K daily revenue", sep=',')
