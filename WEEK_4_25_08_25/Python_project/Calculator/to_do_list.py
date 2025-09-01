# # A to-do list application is a practical project that
#  helps users manage tasks efficiently. This application allows
#  users to add, remove, and view tasks while keeping track of
#  completed and pending activities. Learning to build a to-do
#  list enhances understanding of data structures, file
#  handling, and basic user interaction in Python.
#  This project will cover step-by-step implementation of a to
# do list application, user input handling, list operations, and
#  file handling for persistent storage.

#  Key Concepts of To-Do List in Python
#  Basic List Operations:
#  -Adding tasks
#  -Removing tasks
#  -Marking tasks as complete
#  -Displaying tasks
#  -User Input Handling:
#  -Using input() function
#  -Handling invalid inputs
#  File Handling:
#  -Storing tasks in a text file
#  -Retrieving saved tasks on program
#  restart
#  Functions in Python:
#  -Defining functions for task management
#  -Calling functions with user inputs




# list to store tasks
tasks = []

# define adding function to task
def add_task(task):
    tasks.append(task)
    print(f"Task:", task ,"added!")

# define removing function to task
def rem_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task:", task, "removed!" )
    else:
        print(f"Task Not found!")

# function to display all task
def all_task(tasks):
    if tasks in tasks:
        print(f"All task:", tasks)
    else:
        print(f"Add task!")

while True:
    
    print("select an option:")
    print("1. Add")
    print("2. remove")
    print("3. view task")
    print("4. Exit")
    
    choice = input("Enter an Option (1/2/3):")
    if choice == '1':
        task = input("\nAdd your to-do-list:\n")
        add_task(task)
    
    elif choice == '2':
        task = input("Remove your to-do-list:\n")
        rem_task(task)

    elif choice == '3':
        all_task(tasks)

    elif choice == '4':
        print("Exiting...😃")
        break
    else:
        print("Invalid input")
    

