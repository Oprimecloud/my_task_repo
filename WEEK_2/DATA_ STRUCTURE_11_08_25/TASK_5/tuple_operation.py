# Task 3 tuple operations
# create  a tuple of 5 nigerian sates entered by the user
# input 
nigerian_states = [input("Enter state: "),
                   input("Enter state: "),
                   input("Enter state: "),
                   input("Enter state: "),
                   input("Enter state: ")]

# print first and last state
print(nigerian_states) # displaying user input in tuple
print(nigerian_states[0])
print(nigerian_states[-1])

# check if "lagos" is in the tuple and print "yes" or "no"
print("lagos" in nigerian_states) # yes or "no" True or False

# print the number of states entered
print(len(nigerian_states))
