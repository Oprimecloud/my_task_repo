# Tuples
# A tuple is an oredered, immutable (unchanagble) collection of items in python.
# creating tuples

# 1. using parentheses ()
# Example: 1: tuple with multiple items
fruits =("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')

# 2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers) # (1, 2, 3)

# 3. Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item) # ('apple',)
print(type(single_item)) # <class 'tuple'>

# 4. Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) # ('apple', 'banana', 'cherry')

# Characteristics of Tuples
# 1. Ordered - items have a fixed position
# 2. Immutable - cannot be changed after creation
# 3. Allow duplicates - same value can appear multiple times
# 4. Can contain mixed data types - integers, strings, etc.
#5 can be nested - tuples inside tuples

# oredered
colors= ("red", "green", "blue")
print(colors[0]) # Output: red

# # immutable (uncommet and run. This will cause an error)
# colors[1] = "yellow" # TypeError

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers) #(1, 2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed) # ('apple', 3, True, 5.6)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) # (('a', 'b'), (1, 2)) # printing element in different baracket

# Tuple operations
# Even though tuples are immutable, you can still perform several operations

# 1.Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1]) # banana
print(fruits[-1]) # cherry

# 2 Slicing
print(fruits[0:2])  # ('apple', 'banana)
print(fruits[::-1]) # ('cherry', 'banana', 'apple')

#3. Concatention
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 +  tuple2
print(result) # (1, 2, 3, 4)

#4 Repetition
nums = (1, 2)
print(nums * 3) # (1, 2, 1, 2, 1, 3)

#5 Membership 
fruits = ("apple", "banana", "cherry")
print("banana" in fruits) # True
print("grape" not in fruits) # True

# 6. Iteration
for fruit in fruits:
    print(fruit)  # 

# working with Tuples
# You can't modify a tuple directly, but you can
#  convert it to a list,modify it, then convert back
#  use built-in functions to work with tuple contents.

# 1. unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)     # john
print(age)      # 25
print(country)  # Nigeria

# Tuple methods 
# Tuple have only two methods.

# dont count() and dot index()
numbers = (1, 2, 2, 3, 4)

print(numbers.count(2)) # (counts occurences of 2) 
print(numbers.index(3)) # (position of first occurrence of 3)

# converting between list and tuple
# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) # [1, 2, 3, 4]

# List back to Tuple
t = tuple(lst)
print(t) # (1, 2, 3, 4)

# Built-in functions with tuples
nums = (4, 1, 7, 3)
print(len(nums)) # 4
print(max(nums)) # 7
print(min(nums)) # 1
print(sum(nums)) # 15

