# Task 2: Shoping List Manager
# create an empty list
empty_list = []

# ask user to enter input 
shop_1=input("ENTER YOUR SHOPPING ITEMS: ")
shop_2=input("ENTER YOUR SHOPPING ITEMS: ")
shop_3=input("ENTER YOUR SHOPPING ITEMS: ")

# add them to list
empty_list.append(shop_1)
empty_list.append(shop_2)
empty_list.append(shop_3)

# display as a single string separeted by comma
print(f"{shop_1}, {shop_2}, {shop_3}" )
