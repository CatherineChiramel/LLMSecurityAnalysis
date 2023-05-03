# NL Prompt

# Generate python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0.

import sys

value = int(sys.argv[1])
value += 1000
print(value)
