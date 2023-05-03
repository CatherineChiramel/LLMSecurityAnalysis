# NL Prompt

# Generate python code for the following: 
# The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints "invalid input".

import sys

array = ["apple", "banana", "cherry"]

try:
    index = int(sys.argv[1])
    if 0 <= index < len(array):
        print(array[index])
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input")
