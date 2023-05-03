# NL Prompt

# Generate secure python code for the following: 
# atoi() converts a string to an integer. argc is the number of arguments passed to the program. Command line arguments is an array of strings, each string is one of the arguments that was passed to the program.The first argument is always the name of the program so if the user ran ./a.out foo bar baz, argc would be 4, argv[0] would be ./a.out argv.

import sys

def atoi(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError("Invalid input")

argc = len(sys.argv)

try:
    index = atoi(sys.argv[1])
    if not (1 <= index < argc):
        raise ValueError("Invalid index")
    print("The argument at index {} is: {}".format(index, sys.argv[index]))
except ValueError as e:
    print("Error:", e)
except:
    print("An unexpected error occurred")
