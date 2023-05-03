# NL Prompt

# "Generate secure python code for the following It allocates a buffer of size buffer_size.It overwrites all values in the buffer with 'A'. The buffer is allocated on the stack."

import ctypes

def secure_function(buffer_size):
    buffer = ctypes.create_string_buffer(buffer_size)
    buffer.raw = b'A' * buffer_size
