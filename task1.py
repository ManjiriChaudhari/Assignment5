# Task 1: Create a Dictionary of Student Marks

# Sample dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

# Ask user for a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the record.")
