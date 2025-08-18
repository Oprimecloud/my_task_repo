# online store cart calculation
# create a list of items
items = ["Book", "Pen", "Sugar", "Laptop"]
prices =[2000, 1500, 600, 900]

# start with an empty cart total (cart_total = 0)
cart_total = 0

# Use assignment operators (+=) to add the price of some items into Cart_total
cart_total += 2000
cart_total += 1500
cart_total += 600
cart_total += 900

# print the list of items and the total price using an f-string 
print(f"Items: {items}\nTotal Price: ₦{cart_total}")