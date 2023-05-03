# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0.

import sys

# Read in value from command line
value = int(sys.argv[1])

# Add 1000 to value
value += 1000

# Print value to console
print(value)

# Return 0
sys.exit(0)