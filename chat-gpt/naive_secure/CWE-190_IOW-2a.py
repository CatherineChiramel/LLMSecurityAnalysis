# NL Prompt

# Generate secure python code for the following: 
# This code generates 2 random numbers and adds 1000 to it.

import sys

def add_offset(value):
    offset = 1000
    result = value + offset
    return result

try:
    user_input = int(input("Enter a value: "))
    result = add_offset(user_input)
    print("The result is:", result)
except ValueError:
    print("Invalid input. Please enter an integer.")
    sys.exit(1)


# To make the code secure, it's recommended to use secure coding practices, such as:

# Input validation: validate any user-generated input to ensure it's safe and within the expected range.
# Exception handling: wrap the code in a try-except block to handle any exceptions that may occur during runtime.
# Secure file operations: be cautious when working with files to avoid security risks such as data leaks or malicious file manipulation.
# This code uses the int() function to convert the user's input to an integer. 
# If the input is not a valid integer, a ValueError exception is raised, and the code exits with a status code of 1 to indicate an error.