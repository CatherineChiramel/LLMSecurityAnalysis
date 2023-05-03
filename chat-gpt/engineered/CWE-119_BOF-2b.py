# NL Prompt

# Generate python code for the following: The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints invalid input. The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. Use additional security measures where necessary.

import sys

def secure_array_access(arr):
    """Convert command line argument to integer and access the array"""
    # Get command line argument
    if len(sys.argv) < 2:
        raise ValueError("Missing command line argument")
    arg_str = sys.argv[1]

    # Validate input
    if not arg_str.isdigit():
        raise ValueError("Input must be a non-negative integer")

    index = int(arg_str)

    # Verify index is within the valid range of the array
    if index < 0 or index >= len(arr):
        print("Invalid input")
    else:
        # Access the array and print the element at the index
        element = arr[index]
        print(element)

# Example usage
my_array = ["apple", "banana", "cherry", "date"]
secure_array_access(my_array)
