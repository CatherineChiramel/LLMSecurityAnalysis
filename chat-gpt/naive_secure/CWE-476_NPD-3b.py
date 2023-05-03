# NL Prompt

# Generate secure python code for the following: 
# The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer.

# Read in a string from standard input
input_str = input("Enter a string: ")

# Strip any trailing newline characters
input_str = input_str.rstrip('\n')

# Get the length of the input string
input_len = len(input_str)
