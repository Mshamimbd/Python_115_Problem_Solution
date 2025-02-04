#18. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The root is real and equal: {root}")
    else:
        print("The roots are complex and do not have real values.")


# Taking input from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    solve_quadratic(a, b, c)