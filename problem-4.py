#4. Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.


int_numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(str, int_numbers))
print(string_numbers)