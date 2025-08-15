# Task 2
# unique name collector
#  Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

# input 
attendace_name = set() # name store in set
for i in range(5):
    students =(input("Enter name of people attending a seminar: "))
    attendace_name.add(students)
print(f"unique name: {sorted(attendace_name)}")
