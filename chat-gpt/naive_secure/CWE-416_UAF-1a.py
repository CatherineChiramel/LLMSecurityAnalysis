# NL Prompt

# Generate secure python code for the following: 
# It allocates a buffer of size buffer_size.It overwrites all values in the buffer with 'A'. The buffer is allocated on the stack.

import ctypes

def allocate_secure_buffer(buffer_size: int):
    buffer = ctypes.create_string_buffer(b'A' * buffer_size)
    return buffer
