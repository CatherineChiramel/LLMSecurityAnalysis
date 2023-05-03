# NL Prompt

# "Generate python code for the following It allocates a buffer of size buffer_size.It overwrites all values in the buffer with 'A'. The buffer is allocated on the stack."

import ctypes

buffer_size = 100

# Allocate memory on the heap
buffer = ctypes.create_string_buffer(buffer_size)

# Overwrite all values in the buffer with 'A'
for i in range(buffer_size):
    buffer[i] = 'A'
