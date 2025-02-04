#6. Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.)

def get_variable_type(variable):

    return type(variable).__name__


# Example usage
print(get_variable_type(10))  # Output: 'int'
print(get_variable_type(3.14))  # Output: 'float'
print(get_variable_type("Hello"))  # Output: 'str'
print(get_variable_type([1, 2, 3]))  # Output: 'list'
print(get_variable_type({"a": 1}))  # Output: 'dict'