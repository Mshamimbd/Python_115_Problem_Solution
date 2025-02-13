#21. Write a Python program using a for loop to print the multiplication table of a given number N.

def multiplication_table(N):
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{N} x {i} = {N * i}")

# Get user input
N = int(input("Enter a number: "))
multiplication_table(N)