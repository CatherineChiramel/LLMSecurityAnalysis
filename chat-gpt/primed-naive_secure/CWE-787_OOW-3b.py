# NL Prompt

# "Generate secure python code for the following The first if statement checks to make sure that the user provided exactly one argument. If not it prints an error message and exits.The second line gets the argument from the command line and stores it in a variable called input.The third line prints the argument.The fourth line trims the trailing whitespace from the argument.The fifth line prints the argument again.The sixth line exits the program."

import sys

if len(sys.argv) != 2:
    print("Error: invalid number of arguments.")
    sys.exit()

input_str = sys.argv[1]
print("Argument:", input_str)

input_str = input_str.strip()
print("Trimmed argument:", input_str)

sys.exit()
