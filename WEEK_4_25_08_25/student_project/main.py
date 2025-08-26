#  main.py project entry point

# main.py

import data
import utils

# Add some students
data.add_student("paul", "AI Engineering")
data.add_student("Blessing", "AI Development")

# print formatted student records
for s in data.get_students():
    print(utils.format_student(s))

