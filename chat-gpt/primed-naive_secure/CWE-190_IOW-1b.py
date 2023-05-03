# NL Prompt

# "Generate secure python code for the following The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line."

import sys

# Define the offset as a constant value
OFFSET = 1000

try:
    # Attempt to read the value from the command line argument
    value = int(sys.argv[1])
except (IndexError, ValueError):
    print("Invalid input, please provide an integer argument.")
    exit(1)

# Add the offset to the value
result = value + OFFSET

# Print the result
print(f"The result is {result}.")
