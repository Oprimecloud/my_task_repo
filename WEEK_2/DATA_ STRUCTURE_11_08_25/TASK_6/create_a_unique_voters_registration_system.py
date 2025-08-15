# Task 4
# Create  Unique Voters Registration System
# Ask for voters names and store in a set
voters = set() # store as set
# input 
names = input("Please enter your name(s) to register as a voter:  ")

# if a voter tries to register twice, display a waring
for name in names.split(","):
    name = name.strip()
    if name in voters:
     print(f"⚠️ Warning: {name} is already registered.")
    else:
     voters.add(name)
print(f"{name} has been successfully registered.")

# after registration, display the total number of unique voters.
print(f"Total unique voters registered: {len(voters)}")
print(f"Registered Voters: {sorted(voters)}")