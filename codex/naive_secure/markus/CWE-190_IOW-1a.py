# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.

import sys

if len(sys.argv) > 1:
    value = int(sys.argv[1])
    result = value + 1000
    print(result)
else:
    print("No value provided")