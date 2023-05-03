# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line.

try:
    value = int(input("Enter a value: "))
    offset = 1000
    result = value + offset
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# This code uses a try-except block to handle the possibility of a ValueError being raised when trying to convert the input string to an integer using int. 
# If the input is a valid integer, the code adds an offset of 1000 to it and prints the result. The offset is defined as a constant value that is added to the input value. 
# If the input is not a valid integer, the code will print an error message indicating that the input is invalid.