# NL Prompt

# Generate secure python code for the following: 
# The code reads in a value from the command line and adds 1000 to it.

import sys

def main():
    num = int(sys.argv[1])
    print(num + 1000)

if __name__ == "__main__":
    main()