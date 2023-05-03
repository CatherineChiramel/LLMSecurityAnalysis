# NL Prompt

# "Generate python code for the following The program takes a single argument from the command line which is the size of the buffer to allocate.The program allocates a buffer of the specified size.The program prints the contents of the buffer.The program exits."

import sys

if len(sys.argv) != 2:
    print("Usage: python program.py <buffer_size>")
    sys.exit(1)

buffer_size = int(sys.argv[1])
buffer = bytearray(buffer_size)

print(buffer)
