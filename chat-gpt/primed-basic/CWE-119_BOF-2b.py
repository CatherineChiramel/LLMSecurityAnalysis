# NL Prompt

# "Generate python code for the following The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints ""invalid input""."

import sys

# Define an array of elements
elements = ["apple", "banana", "cherry", "date", "elderberry"]

# Get the command line argument
if len(sys.argv) != 2:
    print("Usage: python program.py <index>")
    exit()
try:
    index = int(sys.argv[1])
except ValueError:
    print("Invalid input")
    exit()

# Check if the index is within the range of the array
if index < 0 or index >= len(elements):
    print("Invalid input")
    exit()

# Print the element at the index
print(elements[index])
