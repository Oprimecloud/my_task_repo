# Single quotes
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''   # to mnake a newline with out \n
print(story)

# String with numbers and symbols
password = "p@sssword123"
print(password)

# string opertions
# indexing
word = "Python"
print(word[0]) # p
print(word[-1]) # n

# Slicing
word = "Python"
print(word[0:4]) # Pyth
print(word[2:])   # thon
print(word[:3])   # Pyt
print(word[::2])  # Pto
print(word[::-1])

# Concatenation

a = "Hello"
b = "world"
print(a + " " + b) # Hello world

# Repetion
word = "Hi! "
print(word * 3) # Hi! Hi Hi!

# String Searching & Checking
# Membership
text = "Python programming"
print("Python" in text) # True
print("Java"  not  in text) # False

# find() / rfind()
text = "Hello World"
print(text.find("o")) # 4 it means to look for letter o in the string what character it falls 
print(text.rfind("o")) # 7 it means to look for letter o in the string what character it falls by ignoring the first letter (o)

# index() / rindex()
text = "Hello world"
print(text.index("world")) # 6 

# startswitch() / endswitch()
filename="data.csv"
print(filename.startswith("data")) # True
print(filename.endswith(".csv")) # True


