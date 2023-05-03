# NL Prompt

# Generate secure python code for the following: 
# The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer.

def scan(format_string):
    buffer = ""
    for character in format_string:
        if character == "\n":
            break
        buffer += character
    return buffer