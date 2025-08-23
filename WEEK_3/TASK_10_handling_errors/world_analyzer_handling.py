# Ask user input 
answer = "northwest"
print("We have 6 Geopolitical zones in Nigeria:")
while True:
    try:
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
            print("\nIncorrect!!! Try again.")
    except KeyboardInterrupt:
        print("\n\n:Warning: you interrupted the quiz. Exiting...")
        break
    except EOFError:
        print("\n\n:warning: Input was closed unexpectedly. Exiting...")
        break
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        break
    