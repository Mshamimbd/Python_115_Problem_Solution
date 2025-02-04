#12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

def find_largest(a, b, c):
    """Function to find the largest among three numbers"""
    largest = max(a, b, c)
    return largest

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding and printing the largest number
largest_number = find_largest(num1, num2, num3)
print(f"The largest number is: {largest_number}")