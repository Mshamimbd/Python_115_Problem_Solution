#20. Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

N = int(input("Enter a positive integer: "))

# Initialize sum
sum_natural = 0

# Loop to calculate the sum of first N natural numbers
for i in range(1, N + 1):
    sum_natural += i

print(f"The sum of the first {N} natural numbers is: {sum_natural}")
