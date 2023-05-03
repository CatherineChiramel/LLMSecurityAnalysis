# NL Prompt

# Generate python code for the following: 
# The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line.

import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide a single input.")
        return
    print(int(sys.argv[1]) + 1000)

if __name__ == "__main__":
    main()