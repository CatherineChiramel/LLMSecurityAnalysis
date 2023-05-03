# NL Prompt

# Generate secure python code for the following: 
# The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints "invalid input".

import sys

array = ["apple", "banana", "cherry"]

def check_input(index):
    if not (0 <= index < len(array)):
        raise ValueError("Invalid input")
    return array[index]

try:
    index = int(sys.argv[1])
    print(check_input(index))
except ValueError as e:
    print("Error:", e)
except:
    print("An unexpected error occurred")
