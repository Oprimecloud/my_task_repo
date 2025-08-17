# Super Market Price List
# Create a program that stores items and their prices in a dictionary.
# Item store in list
Items = ["Rice", "Beans", "Fish", "Meat"]
# user input the price
Item1_price =float(input("Rice price: "))
Item2_price =float(input("Beans price: "))
Item3_price =float(input("Fish price: "))
Item4_price =float(input("Meat price: "))
 
# print(type(Items)) to check type

#  store all item and prices in (store_items)
store_Items = {
    Items[0]: (f"#{Item1_price}"),
    Items[1]: (f"#{Item2_price}"),
    Items[2]: (f"#{Item3_price}"),
    Items[3]: (f"#{Item4_price}")
}
print(f"Store Items and prices are:{store_Items}") # Display all items and prices 

# update price item by user
update_items = float(input(f"updates {Items[2]} price:#"))
store_Items.update({Items[2] :update_items})

# print(f"Store Items and prices are:{store_Items}") # Display updated items and prices 

print(f"Availabe items are : {store_Items.keys()} ")
