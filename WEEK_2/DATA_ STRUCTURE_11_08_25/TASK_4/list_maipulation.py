# Task 7
# list manipulation
# create list
cities = ["peckham", "london","new york","orio","kano"]

# input from user to replace the third
city =input("Enter a city name: ")
cities[2] = city # to replace the third city

# remove the last city
cities.remove("kano") 
print(cities) # ['peckham', 'london', 'oyo', 'orio']

# add a new city to the beginning of the list
cities = ["peckham", "london","new york","orio","kano"]
cities.insert(0, "texas") # insert a new city at the beginnig 

#print the updated list 
print(cities)
