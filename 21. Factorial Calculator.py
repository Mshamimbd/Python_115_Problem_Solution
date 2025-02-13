#21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Get user input
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
