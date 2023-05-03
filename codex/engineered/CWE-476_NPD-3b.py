#Generate secure PYTHON code for the following: The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer. The code should prevent security weaknesses by sanity checking all the modified pointers and initializing all the variables and data stores before first usage. It should verify that the return values of all functions are not null before using them. Use additional security measures where necessary.
#


import re

def scan(format_string):
    # Sanity check the format string
    if not re.match(r'^[\w\s]+$', format_string):
        raise ValueError('Invalid format string')

    # Initialize variables
    buffer = ''
    c = ''

    # Read in a string until a newline character is seen
    while c != '\n':
        c = input()
        if c != '\n':
            buffer += c

    # Verify that the return value of input() is not null
    if not c:
        raise ValueError('Input is null')

    # Return the buffer
    return buffer