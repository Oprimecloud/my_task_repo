# Student Record
# Create an empty dictionary called student
student = {}

# Ask the user to input their name and age and store them in the dictionary
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student = dict(name= name, age = age)

# add a list of scores 
scores = [70, 40,90]
avarage_scores = (scores[0]+ scores[1]+ scores[2])/3


# use a comparison operator to check if the student has passed (avarage score >= 50)
status = (avarage_scores >= 50)
dict(passed = status)

# Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager"
Teenger = (age >= 13) and (age <=19 )

# print out the complete record 
print("\n---")
print(f"Student Record:", "\n""Name:",name, "\n""Age:",age, "\n""Scores:",scores, "\n""Passed:",status, "\n""Teenager:",Teenger)