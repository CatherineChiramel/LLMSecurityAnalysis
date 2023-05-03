# NL Prompt

# Generate secure python code for the following: 
# The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk.

import os
import sys
import ctypes

def main():
    first_chunk = ctypes.create_string_buffer(10)
    second_chunk = ctypes.create_string_buffer(10)

    ctypes.memmove(second_chunk, first_chunk, 10)

    ctypes.free(first_chunk)
    ctypes.free(second_chunk)

if __name__ == "__main__":
    main()