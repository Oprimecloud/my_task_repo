#  Unique Memebers Registration
# Ask the user to enter three names separated by commas
# input from user
user_input = input("Enter 3 names(separated with commas(,)): ").split(",")

# convert them to a set
user_input_set = set(user_input)

# Create a dictionary where each name is a key and its length is the value,
unique_name = {name: len(name) for name in user_input_set}
print(unique_name)