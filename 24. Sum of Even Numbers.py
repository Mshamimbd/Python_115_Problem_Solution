#24. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

N = int(input("Enter a number: "))

sum_even = 0
num = 2  # Start with the first even number

while num <= N:
    sum_even += num
    num += 2  # Increment by 2 to get the next even number

print(f"The sum of all even numbers between 1 and {N} is {sum_even}")