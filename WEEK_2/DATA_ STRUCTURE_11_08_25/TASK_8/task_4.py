# Student Record
# Create an empty dictionary called student
student = {}

# Ask the user to input their name and age and store them in the dictionary
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student = dict(name= name, age = age)

# add a list of scores 
scores1 =70
scores2 =40
scores3 =90
scores = dict(scores1=scores1, scores2=scores2, scores3=scores3 )

print(type(scores))

student = dict(student,scores = scores)
print(student)

# use a comparison operator to check if the student has passed (avarage score >= 50)
