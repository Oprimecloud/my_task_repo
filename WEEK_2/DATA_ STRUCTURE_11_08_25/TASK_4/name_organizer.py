# Task 4 
# Name organizer

# input
name = input("ENTER 5 NAMES (SEPARATED BY SPACES): ") # collect  names input by user

# lower case then split
split_name = name.lower().split(" ") # convert user input to lower case then split

# sort name
split_name.sort()
print(split_name)

# display one name per line 
all_names = [print(f"{name}") for name in split_name]

