# Task1
# Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
# set empty set()
fav_fruits = set()
for i in range(5):
    fruit =input("Enter your favourite fruits: ")
    fav_fruits.add(fruit)
print(f"Your favourite fruits are:{fav_fruits} ")