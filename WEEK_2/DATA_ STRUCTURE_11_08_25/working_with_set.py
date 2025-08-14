# sets in python
# in python, a set is an unordered collection of unique elements.sets are useful when you want to store multiple items but avoid duplicates.

#creating sets
# 1. Using Curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

# 2 using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# 3 creating an empty set (must use set()), not{})
empty_set = set()
print(empty_set)

# 4. from a string (dupliactes removed automatically)
letters = set("mississippi")
print(letters)

# characteristics of sets
# 1. unoredered: No defined indexing or sequence.
# 2. unique elements: Duplicates are automatically removed.
# 3. Mutable: You can add or remove items.
# 4. unindexed: you can't access elements using an index like my_set[0]
# 5. supports mathematical set operations: Union, intersection, difference, symmetric difference

# set operations

# a Adding Elements
colors = {"red", "blue"}
colors.add("green")
print(colors)

# b Removing Elements
colors.remove("red") # Removes an element, raises error if not found
colors.discard("yellow") # Removes an element, raises error if not found
print(colors)

# c pop an element
colors={"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaning:", colors)

# d. Clear a set
colors.clear()
print(colors)

# Mathematical set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. union 
print(set1 | set2 )
print(set1.union(set2))

# 2. Intersection
print(set1 & set2)
print(set1.intersection(set2))

# 3. Difference 
print(set1 - set2)
print(set1.difference(set2))

# 4. Symmetric Difference 
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Working with Sets
# collecting unique visitors ro an event
visitors = set()

# Adding Visiors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# Checking if a visitor attended
# (Dont worry if you can't figure this part out yet. We will discuss it properly later in the course.)

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")
