# TASK 2
# Federal Government Scholarship Key Eligibility Requirements:
# Citizenship Details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

# Citizenship
country_citizen = input("Enter your country: ").upper()

# Enrollment 
institution_confirmation = input("Are you a full-time undergraduate student in a recognized nigerian university(Yes/No): ").upper()

# other scholarships
other_applied_scholarship = input("Do you have any other active scholarship with Oil and Gas industry, whether national or international(Yes/No): ").upper()

# Academic Qualification:
qualification_list = int(input("Enter five distinctions of (As\Bs) in relevant subjects in your WASSCE: "))

#Eligibility
eligibility= (country_citizen == "NIGERIAN") and (institution_confirmation == "YES") and (other_applied_scholarship == "NO") and (qualification_list >= 5)
print(f"Name: {name}\nAge: {age}\nScore: {score}\nCountry: {country_citizen}\nUndergraduate: {institution_confirmation}\nOther Scholarship: {other_applied_scholarship}\nQualification list: {qualification_list}\nYour scholarship eligibility is: {eligibility}")
