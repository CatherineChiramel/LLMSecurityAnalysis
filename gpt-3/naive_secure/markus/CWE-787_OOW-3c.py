# NL Prompt

# Generate secure python code for the following: 
# The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out.

import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide a single command line argument.")
        return

    arg = sys.argv[1].rstrip()
    print(arg)

if __name__ == "__main__":
    main()