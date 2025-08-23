# Ask user input 
answer = "northwest"
print("We have 6 Geopolitical zones in Nigeria:")
while True:
    region = input("Which Geopolitical zone Kano state belongs to: ")
    print(len(region)) # print the length of word
# check if it is all uppercase, all lowercase or title case
    if region.upper() == answer: # check it is in  upper
        print("\n Correct!!!")
    elif region.lower() == answer:
        print("\nCorrect!!!")
    elif region.title() == answer:
        print("\nCorrect!!!")
        break
    else:
        print("\nIncorrect!!!")