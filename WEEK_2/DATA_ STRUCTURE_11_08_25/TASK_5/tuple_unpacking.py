# Task 4 tuple unpacking
# input
user_details = [input(str("What is your firstname: ")),
                int(input("how old are you: ")),
                input(str("what is your favorite color: ")),
                input(str("what state are you from: ")),
                ]    
# store in tuple profile
details =tuple(user_details)
print(details)

# # unpacking tuple
first_name, age, color, state = user_details

# print and use escape sequnce to align each piece of information nicely
print(f" {first_name} \n {age} \n {color} \n {state}")
