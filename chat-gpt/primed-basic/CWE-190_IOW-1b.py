# NL Prompt

# "Generate python code for the following The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line."

import sys

# Define the offset
OFFSET = 1000

# Read a value from the command line
try:
    value = int(sys.argv[1])
except (IndexError, ValueError):
    print("Invalid input")
    exit()

# Add the offset to the value
result = value + OFFSET

# Print the result
print("Result:", result)
