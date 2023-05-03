# NL Prompt

# "Generate secure python code for the following The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out."

import sys

if len(sys.argv) != 2:
    print("Error: expected one argument")
    sys.exit(1)

input_arg = sys.argv[1]
print("Input argument:", input_arg)

# trim trailing whitespace characters
input_arg = input_arg.rstrip()

print("Trimmed argument:", input_arg)
