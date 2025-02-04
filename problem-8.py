#8. String Reversal with Slicing: Write a Python function to reverse a given string using slicing.

def reverse_string(s):
    return s[::-1]

# Example usage
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)  # Output: !dlroW ,olleH