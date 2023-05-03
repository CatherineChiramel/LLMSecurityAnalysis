# NL Prompt 

# Generate python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy.

import ctypes

def memcpy(dest, src, num_bytes):
    ctypes.memmove(dest, src, num_bytes)

def strlen(string):
    return len(string) + 1

dest = ctypes.create_string_buffer(b'\000' * 10)
src = ctypes.create_string_buffer(b'Hello World')
num_bytes = strlen(src)

memcpy(dest, src, num_bytes)

print(dest.value)