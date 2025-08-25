# # # Modularizing Your Code 1
# # # A. Introduction to Modularity

# # What modular programming means
# # Why modularity is important (readability, reusability, debugging, teamwork)

# # What is Modular Programming?
# # - Modular programming is a way of writing programs by dividing them into smaller, independent, and reusable parts (modules) instead of writing one long block of code.
# # - A module can be a function, a class, or a Python file (.py) that performs a specific task.
# # - These modules can then be combined to build a complete program.
# # - In simple words, modular programming `=` breaking big problems into smaller, manageable solutions.

 
# # Why Modularity is Important**
 
# #  - 1. Readability
# #  - Breaking code into smaller modules makes it easier to read and understand.
# #  - Instead of scrolling through hundreds of lines inside a file, you can just put them in different files within a folder and look at the specific file that has the codes you need.
 
# #  - 2. Reusability
# #  - Once you create a module, you can reuse it in different programs.
# #  - No need to rewrite the same code over and over again.
# #  For example, A function that calculates the area of a circle can be used in a school project, an engineering project, or even in a game.

# #  - 3. Debugging and Maintenance
# #  - If there’s an error, you only need to check the specific module where the problem is, instead of combing through the whole program.
# #  - Updating or improving one module doesn’t break the rest of the system.
# #   LEts say, you are building a banking application. If the `payment module` in the app has a bug, the `user login module` is unaffected.

# #  - 4. Teamwork and Collaboration
# #  - In real-world projects, different developers can work on different modules simultaneously.
# #  - Later, all modules are combined into the main project.
# #  - For example,In building a school management system.

# #  One developer handles student records
# #  - Another handles teacher records
# #  - Another handles payment system
# #  - All parts are then combined to make one big system.

# # Lets Put things in perspective
# #   - Imagine we are planning a wedding event. If one person tries to do everything (cook, decorate, handle invitations, music, photography), it becomes chaotic or nearly impossible.
# #   - Instead, tasks are divided:
# #   - The caterer handles food
# #   - The decorator handles decoration
# #   - The DJ handles music
# #   - The photographer handles pictures
# # - At the end, when everyone brings their contribution together, the event runs smoothly.
# # - This is exactly how modular programming works in coding. Each part (module) does its job, and together they form the complete program.

# # # B. Functions (first level of modularity)
# #  - Definition of a function
# #  - Defining and calling functions
# #  - Function parameters and arguments
# #  - Return values
# #  - Use cases (math operations, repeated tasks, formatting output)

# # Definition of a Function
# # - A function is a block of organized, reusable code that performs a single specific task. In python, 
# # we have the inbuilt functions, the user defined functions and lambda function(which is also a type of user defined function)

# # Python Built-in Functions
# # Built-in functions are functions that come pre-installed with Python. You don’t need to import any library to use them. 
# # They are always available, just like how a phone comes with default apps (calculator, messages, clock). And you have used some of them without even knowing.

# # Common Categories of Built-in Functions
# # 1. Input and Output Functions
# # print() # Displays output.
# # input() # Takes user input.

# # 2. Type Conversion Functions
# #  - `int()`, `float()`, `str()`, `bool()`, `list()`, `dict()`, `tuple()`, `set()`

# # 3. Mathematical Functions
# # abs() # Absolute value
# # pow(x, y) # x raised to power y
# # round() # Round numbers to the defined decimal places
# # min(), max() # Find smallest/largest

# # 4. Sequence and Collection Functions
# # len() # Length of a sequence
# # sum() # Sum of elements
# # sorted() # Sort items
# # enumerate() # Track index and value

# # 5. Utility Functions
# # type() # Shows the type of an object(variables,datatypes, data structures, functions, classes)
# # id() # Returns unique ID of object in memory
# # help() # Documentation about an object

# # 6. Special Built-ins
# # range() # Generates a sequence of numbers
# # zip() # Combines two lists element by element
# # map() # Applies a function to all elements in a sequence
# # filter() # Filters elements in a sequence based on condition

# # See Examples of use here
# # range
# for i in range(3):
#     print(i)  #Ouput: 0, 1, 2

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# # It's Ok, if don't know what lambda is  or how to use it. I will touch on it later. Just focus on  the outputs
# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums) # [2, 4]

# # Take a long look at the code below, please
# # Student Performance & Feedback System
# # Step1: Input student data

# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # step 2: store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(name))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of score list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores)) 
# print("\nPassing Scores:", passing)

# # Step 8: map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)

# # I just made use of most of the built-in functions. You can write your own version of this code. Just think through it.

# # User Defined Function

# # Instead of writing the same code again and again, we put it inside a function and just call it whenever we need it.
# # - So functions make programs cleaner, shorter, and easier to manage.
# # - Now, I need you to think of a function like a machine in a factory.
# # - You put something in (input),
# # - The machine works on it (process),
# # - Then gives you something out (output).

# # - In Python, we use the `def` keyword to define a function.
# # Then we call the function whenever we want to use it.
# # - Lets see the function structure
# # def function_name(takes in input):
# #     process block
# #     output block

# # - More explanation
# # def function_name(input - here, you will insert an item or list of what the function will need to work):
# #   "process block -here will contain the logic or what you want the function to do"
# #   " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or'print()' or 'yield'"

# Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# # And you can call it as many times as possible.
# greet()
# greet()
# greet()

# # Function Arguments and Parameters

# # - Arguments are variables you add inside the function parenthesis when defining the function (placeholders). Sometimes, they can be optional.
# # - Parameters are the actual values you pass inside the function parenthesis when calling the function.

# Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "Welcome to Python learning!")

# # Calling with parameter - the actual name
# greet("Class rep")
# greet("Ridwan")

# When to Use `return`, `print()`, and `yield` keywords inside a function

# a. print()
#  - You can use it if you are just interested in displaying your output (Not Storing). It does not give back a value you can use later.
#  - Think of it like shouting information out loud, but not recording it for reference purpose.
#  - So you use it when you just want to show results to the user.  Example: printing menus, reports, or logs. 

# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)

# b. return
#  - You can use it if you want to give back a value.
#  - `return` sends a value back to the function caller.
#  - The function ends immediately once it hits return.
#  - Think of it like filling a form and handing it back, the caller now owns the result and can reuse it.
#  - So you can use `return` when you need the result for further computation or storage.For example, math calculations, data processing, formatting text.

def add(a, b):
    return a + b

# Function call 

result = add(4, 6)
print("The Sum is:", result)

# Note the Output and compare it with that of print()

# 3. yield
#  – This is used for producing a Sequence (Generators)
#  - `yield` works like return, but instead of ending the function, it pauses it and remembers its state.
#  - Next time you call it, it resumes from where it stopped.
#  - This creates a generator. 
#  - You can use it when working with large data or infinite sequences. 

def count_up_to(n):
    i = 1
    while i <= n:
        yield i # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.

# ore on Function Arguments(Types of Arguments)
# - Functions can accept different types of arguments depending on how we want to pass data. Understanding these makes functions flexible and powerful.

# 1. Positional Arguments
# - These are the most common.
# - The order matters: values are assigned to parameters in the same order as they appear.
# - Think of it like lining up children in the same order as roll call

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce("Ngozi", "AI Engineering")  # Correct order

# Change the arrangment and watch the output

introduce("AI Engineering", "Ngozi")   # Incorrect order, this will throw a semantic error

# 2. Keyword Arguments
# - Here, you explicitly mention the parameter name when calling the function.
# - Order doesn’t matter, since Python knows which value goes where.
# - Think of it like addressing an envelope by name instead of position in line.

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the ouput
introduce(track = "AI Engineering", name = "Ngozi")    # Here you notice that order does not matter

# 3. Default Arguments
# - Here, you can give parameters a default value.
#  - Even if no value is provided when calling, the default is used.
#  - Think of it like a restaurant menu where rice is served by default if you don’t choose otherwise.

def introduce(name, track = "AI Enginerring"):
    print("My name is", name)
    print("I am learning", track,".")

#  function call
#  Without specifying the default argument, but watch the ouput
introduce("Paul")

# Specify the default argument and watch the output
introduce("Tunji Paul", track = "AI Development")

# 4. Varying Length Arguments
# - Sometimes we don’t know how many arguments will be passed. Python provides two special symbols(that is the asterisk)
#  - single asterisk for non-keyword arguments or tuple(*args)
#  - Double asterisk for keyword arguments or dictionary(**kwargs)

# a. non-keyword (tuple)
# - Collects extra positional arguments into a tuple.
# - Think of it like packing extra clothes into a bag.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
        print("Sum:", total)

# function call
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# b. keyword argument (dictionary)
# - Collects extra keyword arguments into a dictionary.
# - Think of it like a labeled container where each item has a name tag.

def student_details(**Kwargs):
    for key, value in Kwargs.items():
        print(key, ":", value)

# function call - Take note of the output
student_details(name="peter", track = "AI Engineering", interest = "Block Chain")

# Lets implement on full code

# Define student profile function
# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it if you are using everything or some of it together

def participant_profile(name, age, track ="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n---Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age:   {age}\n"
    profile += f"Track: {track}\n"

    # Skills (From *args)
    if skills:
        profile += "Skiils: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    return profile # Do you remember 'return' and why it is used? we are using it so it can be reused in other places

# --------------LETS test ---------------
# Exanple 1: Using only positionla arguments
print(participant_profile("Peter", 24))

# Example 2: Adding Keyword / default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments   (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="shagamu", phone="08123456789"

))

# Namespaces and Scope
# Namespace
# - A namespace is like a “container” that holds names (variables, functions, objects) and maps them to the actual data stored in memory.
# - Think of it as a dictionary where keys are names and values are objects.
# - Python uses namespaces to avoid name conflicts.
# - Lets imagine a company where different departments can have employees with the same name.
# - In the IT department, there may be a "Chris".
# - In the Training department, there may also be a "Chris".
# - Both exist, but they are identified by their department (namespace), so there’s no confusion.

# Types of Namespaces 
#  - 1. Built-in namespace -Provided by Python (e.g., len, print, list).
#  - 2. Global namespace -Names defined at the top level of a script or module.
#  - 3. Local namespace -Names created inside a function.

#  Global Namespaces
employee = "General Employee"

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)
def Training_department():
    # Local Namespace inside Training_department
    employee = "Chris (Training)"
    print("Inside Trainig Department:", employee)
print("In Global Namespaces:", employee)  # Refers to global variable

IT_department()  #  Uses local variable in IT
Training_department() # Uses local variable in Training

# Using a built-in namespace function
print("Length of 'Python':", len("Python"))

# So 'Chris' can exist in more than one namespace without conflict.
# Please, take your time to study the output carefully.


# Scope
# - Scope defines where in the code a name is accessible.
# Python follows the *LEGB Rule* (order of search for a variable):

# L – Local → Inside the current function.
# E – Enclosing → Inside any enclosing function(s).
# G – Global → At the top level of the script/module.
# B – Built-in → Python’s built-in functions/objects.

x = "global x" # Global Namespace

def outer():
    x = "enclosing X"   #  Enclosing Namespace
    def inner():
        x = "local x"    # Local Namespace
        print("Inside inner:", x)   # Local wins
    inner()
    print("Inside outer:", x)   # Enclosing
outer()
print("In global:", x)  # Global

# Watch the output
# Notice how Python searches in the order Local → Enclosing → Global → Built-in (LEGB).

# Global keyword
# Used when you want to modify a global variable inside a function.
x = 5
def change_global():
    global x
    x = 10 # modifies the global x

change_global()
print(x)       # Output: 10

# Watch the output

# nonlocal keyword
# used in nested functions when you want to modify the variable from the enclosing scope (not global),

def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "changed by inner"
        print("Insider inner:", x)

    inner()
    print("Insider outer:", x)
outer()

# Watch the output

# So understanding namespace and scope helps avoid name conflicts, makes modular code easier to read, 
# and ensures functions and modules can work without interfering with each other.

# Lamda Function
# - A lambda function is a small, anonymous function (no name) defined using the lambda keyword.
# - It can have any number of arguments, but only one expression.
# - The result of the expression is automatically returned.

# This is the syntax
# lambda arguments: expression

# You use lambda;
# - When you need a short, throwaway function(not reuseable).
# - To avoid writing full def functions for small tasks.
# - Used with functions like map(), filter(), sorted(), and reduce().

# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))
# Watch the output and note the difference

# This one has more that one arguments.
add = lambda a, b: a + b
print(add(3, 7)) # Ouput: 10


# Let use lambda to apply the square function to a list
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Ouput: [1, 4, 9, 16]

# Lets use lambda to filter even numbers
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 ==0, numbers))
print(evens) # Output: [10, 20, 30]

students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# ouput: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse = True)
print(students_sorted_descending)
# Output: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)
# Output: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]