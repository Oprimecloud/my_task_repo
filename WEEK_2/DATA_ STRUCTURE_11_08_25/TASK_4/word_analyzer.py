# Task 6 word analyzer
# input 
word = input("Enter a word: ")
print(len(word)) # print the length of word

# check if it is all uppercase, all lowercase or title case
is_upper =word.isupper() # check it is in  upper
is_lower =word.islower() # check it is in lower
is_title =word.istitle() # check it is in title
print(f"{is_upper}")
print(f"{is_lower}")
print(f"{is_title}")

# Reverse the word using slicing
print(word[::2])   # reverse the word