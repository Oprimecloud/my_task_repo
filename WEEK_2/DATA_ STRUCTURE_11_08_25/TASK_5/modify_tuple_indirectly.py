# Task 5
# modify tuple indirectly 
# ask a user to enter three items for their shopping list.
# input
items= (
       input(str("Enter your shopping list: ")),
       input(str("Enter your shopping list: ")),
       input(str("Enter your shopping list: "))
       ) # store the user in tuple format
# print(items) # to check the user input in tuple format

# convert tuple to list
conv_item_to_list = list(items)
# print(conv_item_to_list) # to check if it has been conver to list

# ask for more 2 extra
conv_item_to_list.append(input("Add more shopping list: ")) # asking user to add more items
conv_item_to_list.append(input("Add more shopping list: ")) # asking user to add more items

# convert back to a tuple
updated_items = tuple(conv_item_to_list) # convert list to tuple
print('|'.join(updated_items))

