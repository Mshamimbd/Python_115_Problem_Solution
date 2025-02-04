#9. String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the + operator.

def concatenate_strings(str1, str2):
    return "".join([str1, str2])

# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenating strings
result = concatenate_strings(string1, string2)

# Display the result
print("Concatenated String:", result)