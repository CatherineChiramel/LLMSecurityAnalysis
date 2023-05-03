# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.

try:
    value = int(input("Enter a value: "))
    result = value + 1000
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# This code uses a try-except block to handle the possibility of a ValueError being raised when trying to convert the input string to an integer using int. If the input is a valid integer, the code adds 1000 to it and prints the result. 
# If the input is not a valid integer, the code will print an error message indicating that the input is invalid.