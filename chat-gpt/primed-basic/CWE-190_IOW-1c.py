# NL Prompt

# "Generate python code for the following The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0."

import sys

# Read a value from the command line
try:
    value = int(sys.argv[1])
except (IndexError, ValueError):
    print("Invalid input")
    exit()

# Add 1000 to the value
result = value + 1000

# Print the result to the console
print("Result:", result)

# Return 0
exit(0)
