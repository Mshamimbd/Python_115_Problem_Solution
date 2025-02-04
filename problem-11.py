#11. Python Conditional Statements: Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Take user input
try:
    number = float(input("Enter a number: "))
    check_number(number)
except ValueError:
    print("Invalid input! Please enter a numeric value.")