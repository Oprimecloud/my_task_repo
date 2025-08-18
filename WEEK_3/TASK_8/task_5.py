# store Inventory Update
# create a dictionary called store with items and their availabe quantities.
store = {"Fish":10, "Meat":30, "Rice":45, "Beans":75} 
print("Available items in stock include Fish, Meat, Rice and Beans")

# Ask user to input the item they want to buy
user_input_item = input("Enter what item you want to buy: ").title()
user_input_quantity = int(input("Enter the qauntity of item: "))
print(f"Before purchase: {store}")

# use the assignment operator 
store[user_input_item] -= user_input_quantity

# updated dictionary 
print(f"After purchase: {store}")


