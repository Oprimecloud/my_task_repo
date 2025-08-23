# file 8

# Transport fare calculator
distance =float(input("ENTER YOUR DISTANCE IN KILOMETER: "))
tfare = float(input("HOW MUCH YOU SPEND PER KILOMETER: "))

# total fare = (distance * tfare)
print(f"Distance: {distance} km")
print(f"Fare per km: ₦{tfare}\km")
print(f"Total fare:",f"₦{tfare * distance:.2f}")


