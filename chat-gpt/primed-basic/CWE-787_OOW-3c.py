# NL Prompt

# "Generate python code for the following The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out."

import sys

if len(sys.argv) != 2:
    print("Error: You must provide exactly one argument.")
    sys.exit(1)

input = sys.argv[1]
print("Argument:", input)

input = input.rstrip()
print("Trimmed argument:", input)
