# Task 2 tuple and input
# input from user
fr_best_name = [
    input("Enter your five best friends' names: "),
    input("Enter your five best friends' names: "),
    input("Enter your five best friends' names: "),
    input("Enter your five best friends' names: "),
    input("Enter your five best friends' names: ")]

# store them in a tuple friends.
tup = tuple(fr_best_name)
print(tup)

# print the tuple in reverse order.
print(tup[::-1])