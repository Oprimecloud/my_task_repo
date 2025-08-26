# Modularizing Your Code 2

# 3. Python Modules

# What a module is (a.py file that can be reused)
# Importing built-in modules (math, random, datetime)
# Writing your own module (creating my_module.py and importing it)
# Aliasing modules (import numpy as np)

# What is a module?
# A module in Python is simply a file with .py extension that contains Python code (functions, variables, or classes) which can be reused in other programs.
# Instead of writing the same code again and again, you can write it once in a module and then import it anywhere.
# LEts think of a module as a toolbox. Each tool (function, variable, or class) can be taken out and used whenever needed, without rebuilding the tool from scratch.

# Importing Built-in Modules
# - Python already comes with many pre-built modules that you can use directly.
# - Some common examples are:
# - math -for mathematical operations
# - random - for generating random numbers
# - datetime - for working with dates and time.
# - etc.
# - To use built in modules, you have to load them into your environment, that is, `import` them.

# Different Ways to Import Modules

#1. Import the whole module
import math

# Lets put it to use
print(math.sqrt(9))
# - Note that you must specify the module name when calling a function within it.

# 2. import as an alias

import math as m

# lets put it to use

print(m.sqrt(25))

# - This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables
from math import sqrt, pi

print(sqrt(36))
print(pi)

# - here you dont need the prefix 'math.' anymore

# 4. Import everything from the module

from math import *
print(sqrt(49))
print(pi)
# - This is usually not recommended because it can cause name conflits if two modules have functions with the same name

# Writing Your Own Module
# - step1: Create a folder. Name it my_module
# - step2: Create a file inside the folder. Name it first.py
# - step3: Create another file inside the same folder. Name it second.py
# - Step4: Create another file still inside the same folder. Name it main.py

#  - here is the folder structure
# ```
# project_folder/
# │
# ├── my_module/
# │   ├── first.py
# │   ├── second.py
# │   └── main.py
# ```
# - Note that anyone with forward slash is a folder while the ones with extensions are the files.