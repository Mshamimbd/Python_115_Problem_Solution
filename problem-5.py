#5. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Take user input
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
