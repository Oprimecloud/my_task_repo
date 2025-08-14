# Tuple Practice
# Task 1 create and display
# input

dish = input("Enter a Nigerian dish name: ")
dish_1 = input("Enter a Nigerian dish name: ")
dish_2 = input("Enter a Nigerian dish name: ")

# store them in tuple called dishes
tup = tuple(dish)
tup = tuple(dish_1)
tup = tuple(dish_2)
dishes = (dish, dish_1 , dish_2) # store all dish in tuple called dishes

# # print the tupple in a single line, separating items commas.
print("your typed dishes are:", dishes)

# use the \n ecsape sequence to print each dish on a new line.
print("", dish,"\n",dish_1,"\n", dish_2)
