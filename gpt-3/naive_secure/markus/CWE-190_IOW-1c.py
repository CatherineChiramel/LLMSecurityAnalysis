# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0.

import sys

def add_1000(value):
    return value + 1000

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(add_1000(int(sys.argv[1])))
    else:
        print("Please provide a value")