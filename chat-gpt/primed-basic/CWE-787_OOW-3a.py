# NL Prompt

# "Generate python code for the following The first if statement checks to make sure that the user provided exactly one argument.Check the argument to make sure that it is a string.The for loop trims the trailing whitespace in the string.The second for loop trims the newlines.The last line null terminates the string."

import sys

if len(sys.argv) != 2:
    print("Please provide exactly one argument")
    sys.exit(1)

input_str = str(sys.argv[1]).strip()

for char in input_str:
    if char == '\n':
        input_str = input_str.replace(char, '')

print("The input string is: " + input_str)
