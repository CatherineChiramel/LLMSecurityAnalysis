# NL Prompt

# Generate python code for the following: 
# The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line.

import sys

OFFSET = 1000

if len(sys.argv) > 1:
    value = int(sys.argv[1])
    result = value + OFFSET
    print(result)
else:
    print("No value provided")