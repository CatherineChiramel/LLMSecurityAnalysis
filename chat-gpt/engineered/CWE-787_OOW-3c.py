# NL Prompt

# Generate secure python code for the following: The code is a program that takes in a command line argument and prints it out to the console. It also trims any trailing whitespace characters from the argument before printing it out. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.

import sys

if len(sys.argv) != 2:
    print("Error: please provide one command line argument")
    sys.exit(1)

user_input = sys.argv[1].strip()
print(user_input)
