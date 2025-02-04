#17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle

def classify_triangle(a, b, c):
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or a == c or b == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a valid triangle"


# Take input from the user
try:
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    # Print the classification result
    print("Triangle Type:", classify_triangle(a, b, c))
except ValueError:
    print("Invalid input! Please enter numerical values.")
