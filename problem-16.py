#16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

try:
    hour = int(input("Enter the time in hours (0-23): "))
    if 0 <= hour <= 23:
        print(get_greeting(hour))
    else:
        print("Please enter a valid hour between 0 and 23.")
except ValueError:
    print("Invalid input! Please enter a numerical value between 0 and 23.")