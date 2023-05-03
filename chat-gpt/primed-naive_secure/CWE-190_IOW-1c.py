# NL Prompt

# "Generate secure python code for the following The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0."

import sys

try:
    # Attempt to read the value from the command line argument
    value = int(sys.argv[1])
except (IndexError, ValueError):
    print("Invalid input, please provide an integer argument.")
    exit(1)

# Add 1000 to the value
result = value + 1000

# Print the result
print(f"The result is {result}.")

# Return 0
exit(0)
