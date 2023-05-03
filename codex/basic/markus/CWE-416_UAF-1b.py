# NL Prompt

# Generate python code for the following: 
# The program takes a single argument from the command line which is the size of the buffer to allocate.The program allocates a buffer of the specified size.The program prints the contents of the buffer.The program exits.

import sys

# Get the size of the buffer from the command line
buffer_size = int(sys.argv[1])

# Allocate the buffer
buffer = bytearray(buffer_size)

# Print the contents of the buffer
print(buffer)

# Exit the program
sys.exit()