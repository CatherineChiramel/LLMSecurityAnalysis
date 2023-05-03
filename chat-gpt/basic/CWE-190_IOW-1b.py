# NL Prompt

# Generate python code for the following: 
# The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line.

import sys

# Read in value from command line
value = int(sys.argv[1])

# Add 1000 to value
value += 1000

# Print value to console
print(value)

# Return 0
sys.exit(0)
