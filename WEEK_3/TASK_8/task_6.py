#  UNILAG Admission Eligibility 
'''
- Ask for user's name
- Ask your for their UTME score
- Prompt them to choose UNILAG as the first choice of institute
- Ask for the O'level result of at least 5 credit in English amd Mathematics and other relevant subjects in a siting 
- Check if the user meets all the requirements
-Then print out the eligibility status
'''
candidate_name = input("Enter your name: ")

UTME_score = int(input("Kindly enter your UTME Score: "))

uni_choice = input("Did you choose UNILAG as first choice: ").title()

Olevel_result = input("Do you have five credit in relevant O'level subjects including Mathematics and English at one sitting?: ").title()

eligibility = (UTME_score >=200) and (uni_choice == "Yes") and (Olevel_result == "Yes")

print(f"{candidate_name} eligibility status is {eligibility}.")