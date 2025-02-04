#19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

def check_range(number):
    if 0 <= number <= 50:
        print("The number falls within the range 0-50.")
    elif 51 <= number <= 100:
        print("The number falls within the range 51-100.")
    elif 101 <= number <= 150:
        print("The number falls within the range 101-150.")
    else:
        print("The number is above 150.")

# Taking user input
try:
    num = int(input("Enter an integer: "))
    check_range(num)
except ValueError:
    print("Invalid input! Please enter an integer.")