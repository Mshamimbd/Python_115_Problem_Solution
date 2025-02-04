#14. Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

def determine_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

# Taking user input
try:
    percentage = float(input("Enter student's percentage: "))
    if 0 <= percentage <= 100:
        print("Grade:", determine_grade(percentage))
    else:
        print("Please enter a valid percentage between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
