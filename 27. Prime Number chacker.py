#27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

def is_prime(N):
    if N < 2:
        return False

    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


# Input from the user
N = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(N):
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")