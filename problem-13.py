#13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Take user input
year = int(input("Enter a year: "))

# Check if it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
