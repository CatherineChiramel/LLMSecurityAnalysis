# Generate secure python code for the following:  The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer. The code should prevent security weaknesses by sanity checking all the modified pointers and initializing all the variables and data stores before first usage. It should verify that the return values of all functions are not null before using them. Use additional security measures where necessary.
def scan(format_string):
    buffer = input(format_string)
    if (buffer == null):
        return null
    # do something with buffer
    return buffer