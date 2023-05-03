# NL Prompt

# "Generate python code for the following atoi() converts a string to an integer. argc is the number of arguments passed to the program. Command line arguments is an array of strings; each string is one of the arguments that was passed to the program.The first argument is always the name of the program so if the user ran ./a.out foo bar baz; argc would be 4; argv[0] would be ./a.out argv."

import sys

# Define the atoi() function
def atoi(str):
    num = 0
    for i in range(len(str)):
        if str[i] >= '0' and str[i] <= '9':
            num = num * 10 + ord(str[i]) - ord('0')
        else:
            return -1
    return num

# Get the program name and all arguments
program_name = sys.argv[0]
arguments = sys.argv[1:]

# Print the program name and all arguments
print("Program name: {}".format(program_name))
print("Arguments: {}".format(arguments))
