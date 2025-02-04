#15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

def check_character_type(char):
    vowels = 'aeiouAEIOU'
    if len(char) == 1 and char.isalpha():
        if char in vowels:
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetic character.")

# Get user input
char = input("Enter a single character: ")
check_character_type(char)