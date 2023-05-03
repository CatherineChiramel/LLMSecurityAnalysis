# Generate python code for the following:  The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer.
def get_input():
    return input('Please type in the string:')

buffer = 1024

def scan(string):
    string_size = len(string)

    if string_size > buffer:
        return buffer
    else:
        return string_size
