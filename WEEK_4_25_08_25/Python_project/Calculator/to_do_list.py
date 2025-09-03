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

TASKS_FILE = "Task.txt"
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:

        tasks = []
    return tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
tasks = load_tasks()


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

# function to edit task
def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    else:
        print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    try:
        task_num = int(input("Enter the number of \'to-do-list\'you want to edit "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new \'to-do-list\' description: ")
            tasks[task_num - 1] = new_task
            print("\'To-do-list\' updated seccessfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("please enter a valid number. ")

# function to display all task
def all_task(tasks):
    if tasks:
        for idx, task in enumerate(tasks,1):
            print(f"{idx}. {task}")
    else:
        print(f"No tasks in yor list!")

while True:
    print("\n----------TO D0 lIST----------------")
    print("\tselect an option:")
    print("1. Add \'to-do-list\'")
    print("2. view \'to-do-list\'")
    print("3. edit \'to-do-list\'")
    print("4. remove \'to-do-list\'")
    print("5. Exit")
    print("--------------------------------------")    
    choice = input("Enter an Option (1/2/3):")
    if choice == '1':
        task = input("\nEnter to Add \'to-do-list\':\n").title()
        add_task(task)
        save_tasks(tasks)

    elif choice == '2':
        all_task(tasks)
    
    elif choice == '3':
        edit_task(tasks)
        save_tasks(tasks)

    elif choice == '4':
        task = input("Enter to Remove \'to-do-list\':\n").title()
        rem_task(task)

    elif choice == '5':
        print("Exiting...😃")
        break
    else:
        print("Invalid input")

    

