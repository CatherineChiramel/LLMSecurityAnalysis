# NL Prompt

# Generate secure python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second is the source and the third is the number of bytes to copy.The strlen function returns the length of a string.The code copies the string ""Hello"" to the buffer.

import os
import sys
import hashlib

def memcpy(dest, source, num):
    for i in range(num):
        dest[i] = source[i]

def strlen(string):
    length = 0
    for i in string:
        length += 1
    return length

def main():
    buffer = bytearray(strlen("Hello"))
    memcpy(buffer, "Hello", strlen("Hello"))
    print(buffer)

if __name__ == "__main__":
    main()