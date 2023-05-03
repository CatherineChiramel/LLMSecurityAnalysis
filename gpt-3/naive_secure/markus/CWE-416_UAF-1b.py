# NL Prompt

# Generate secure python code for the following: 
# The program takes a single argument from the command line which is the size of the buffer to allocate.The program allocates a buffer of the specified size.The program prints the contents of the buffer.The program exits.

import sys

size = int(sys.argv[1])

buffer = bytearray(size)

for i in range(size):
    buffer[i] = i & 0xff

print(buffer)