#7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True