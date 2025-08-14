# Task 5: Student Score Tracker
# empty list
name = [] # empty list for name
score = [] # empty list for score
 
# input
nam =input("Enter name: ") # first collection data on name
nam_1 =input("Enter name: ") # second collection data on name
nam_2 = input("Enter name: ") # third collection data on name 
scr = input("Enter score: ") # first collection data on score 
scr_1 = input("Enter score: ") # second collection data on score
scr_2 = input("Enter score: ") # Third collection data on score

# result store in two list name & score
name.append(nam) # add to the list name 
name.append(nam_1) # add to the list name
name.append(nam_2)  # add to the list name

score.append(scr) # add to the list score
score.append(scr_1) # add to the list score
score.append(scr_2) # add to the list score

# display a formatted output showing Name -- Score 
print("Name\t | Score")
print("-"*20)
print(f"{name[0]} \t | {score[0]}")
print(f"{name[1]} \t | {score[1]}")
print(f"{name[2]} \t | {score[2]}")


