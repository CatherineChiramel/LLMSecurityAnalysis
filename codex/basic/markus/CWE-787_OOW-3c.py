# NL Prompt

# Generate python code for the following: 
# The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out.

import sys

# Get the command line argument
argument = sys.argv[1]

# Trim any trailing whitespace characters
argument = argument.rstrip()

# Print the argument
print(argument)