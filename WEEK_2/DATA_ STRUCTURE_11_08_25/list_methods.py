### List Methods
# python provides many built-in methods to work with lists. Here is each method, whatit does, and an example

# 1. dot append() method
# adds an element to the end of the list.

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# output: ['apple', 'banana', cherry]

# 2. dot insert() method 
# inserts an element at a specific position

fruit = ["apple", " banana"]
fruits.insert(1, "orange")
print(fruits)
# Output: ['apple', 'orange', 'banana']

# 3. dot extend() method
# adds elements from another list (or iterable) to theend

fruits = ["apple", "banana"]
tropical =["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)
# Output: ['apple', 'banana', 'mango', 'pineapple']

# 4. dot remove() method
# removes the first occurrence of a specified value
fruits = ["apple", "cherry", "banana"]
fruits.remove("banana")
print(fruits)
# output: ['apple', 'cherry', 'bannana']

# 5. dot pop() method
# removes and returns the element at a given index (default:last)
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)
# output: cherry
print(fruits)
# output: ['apple', 'banana']

# 6. dot clear() method
# removes all elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# output: []

# 7. dot index() method
# returns the index of the first occurrence of a value
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)
# output: 1

# 8. dot count() method
# counts how many times a value appears
fruits = ["apple", "banana", "cherry", "banana"]
# output: 2

# 9. dot sort() method
# sorts the list in ascending order by default
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  
# Output: [1, 2, 3, 4]

# descending order
numbers.sort(reverse=True)
print(numbers)  
# Output: [4, 3, 2, 1]

#  *10. dot reverse() method**
#  Reverses the order of the list.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  
# Output: ['cherry', 'banana', 'apple']

# 11. copy()
# - Returns a shallow copy of the list(This should be familiar already)
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)  
# Output: ['apple', 'banana', 'cherry']