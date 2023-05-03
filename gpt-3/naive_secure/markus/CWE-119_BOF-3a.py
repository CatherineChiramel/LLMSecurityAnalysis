# NL Prompt

# Generate python code for the following: 
# atoi() is a function that converts a string to an integer. Command line arguments at index 1 is the second argument passed to the program. Command line argument at index INDEX is the argument at the INDEX specified by the second argument. print function prints the string at INDEX position in the command line arguments to the screen. return 0. exit the program.

#!/usr/bin/env python

import sys

def atoi(s):

    """

    Converts a string to an integer.

    Arguments:
    s - the string to convert

    Returns:
    the integer value of the string

    """

    if not s:
        return 0

    i = 0

    for c in s:

        if c.isdigit():
            i = i * 10 + int(c)

        else:
            break
    return i

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: atoi.py <string>')
        sys.exit(1)

    print(atoi(sys.argv[1]))
    sys.exit(0)