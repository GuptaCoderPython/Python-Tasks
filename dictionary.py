# Task 1: Create a dictionary with student ID and names
students = {
    "S001": "Neeraj",
    "S002": "Gupta",
    "S003": "Vansh",
    "S004": "Tarun",
    "S005": "Sachin"
}

# Task 2: Adding a new student to the dictionary
students["S006"] = "Manish"

# Task 3: Updating the name of an existing student
students["S002"] = "Rahul"

# Task 4: Accessing a student's name by their ID
print(students["S003"])

# Task 5: Creating a nested dictionary with student details
students_details = {
    "S001": {"name": "Neeraj", "age": 20, "grade": "A"},
    "S002": {"name": "Rahul", "age": 22, "grade": "B"},
    "S003": {"name": "Vansh", "age": 21, "grade": "C"},
    "S004": {"name": "Tarun", "age": 23, "grade": "B"},
    "S005": {"name": "Sachin", "age": 19, "grade": "A"}
}

# Task 6: Accessing values from the nested dictionary
print(students_details["S003"]["name"])
print(students_details["S002"]["grade"])

# Task 7: Printing the keys of the dictionary
print(list(students_details.keys()))

# Task 8: Deleting a student entry from the dictionary
del students_details["S004"]

print(students_details)