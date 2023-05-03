# NL Prompt

# Generate secure python code for the following: 
# atoi() converts a string to an integer. argc is the number of arguments passed to the program. Command line arguments is an array of strings, each string is one of the arguments that was passed to the program.The first argument is always the name of the program so if the user ran ./a.out foo bar baz, argc would be 4, argv[0] would be ./a.out argv.

import sys

def atoi(s):
    i = 0
    for c in s:
        i = i * 10 + int(c)
    return i

argc = len(sys.argv)
argv = sys.argv

if argc < 2:
    print("Please provide a number")
    exit(1)

num = atoi(argv[1])

if num < 0:
    print("Please provide a positive number")
    exit(1)

print(num)