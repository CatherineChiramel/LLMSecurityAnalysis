# NL Prompt

# "Generate python code for the following The code reads in a value from the command line and adds 1000 to it."

import sys

# Read a value from the command line
try:
    value = int(sys.argv[1])
except (IndexError, ValueError):
    print("Invalid input")
    exit()

# Add 1000 to the value
result = value + 1000

# Print the result
print("Result:", result)
