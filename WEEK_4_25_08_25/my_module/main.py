# my_module/main.py
import first
import second

# lets use the functions in the first.py file
print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets use the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python'=", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))

# 5. Code Reusability
# What is Code Reusability?
# - Code reusability means writing code once and using it multiple times instead of rewriting it.
# - It helps make programs cleaner, faster to develop, and easier to maintain.
# - In Python, code reusability is achieved using;

#  - Functions (reusing blocks of code)
#  - Modules (saving functions in .py files to import later)
#  - Packages (organizing modules in folders)
#  - Classes & Objects (OOP makes reusable blueprints)
#  - Libraries (built-in or third-party)

# Why Reuse Code?

# - Saves time – no need to rewrite the same logic.
# - Avoids duplication – reduces errors from copy and paste.
# - Improves readability – your code is modular and organized.
# - Easy to maintain – update once, reuse everywhere.

# 6. Organizing a Python Project
# - A modular project is a way of organizing your code into separate files and folders, each responsible for a specific task.
# - This makes the project easier to read, test, and maintain.

# Why Use Modular Structure?
# - Separates concerns – Each file has one responsibility.
# - Easier to debug – You can fix issues in one place without breaking others.
# - Reusability – Functions/modules can be reused in other projects.
# - Collaboration-friendly – Multiple developers can work on different parts.

