# Task 3
# Simulate a football match ticket system
# store input in set
seat_numbers = set(range(1, 51))
print(f"Available booking seat: {seat_numbers}")

# asking user to "book" using input
booking = input("Kindly input your booking seat number: ")

# removed booked seats number from the set
seat_numbers.remove(int(booking))
print(f"Your seat number {booking} has been successfully booked ") # showing user booked number
print(f"Remaining seats booking: {seat_numbers}") # showing user the remaining seats number

