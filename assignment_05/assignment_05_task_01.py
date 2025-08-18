# Assignment 5:
# Module 6: Data Structures and Strings in Python
# Task 1: Create a Dictionary of Student Marks

marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 75,
    "Daniel": 60,
    "Eve": 55
}

name_to_search = (input("Enter the student's name: ")).strip()

print ("{}'s marks: {}".format(name_to_search, marks['Alice']) if (name_to_search in marks) else "Student not found.")
