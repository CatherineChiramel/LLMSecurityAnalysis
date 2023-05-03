# NL Prompt

# Generate secure python code for the following: 
# The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk.

import ctypes

# Allocate two chunks of memory each of size 10
first_chunk = ctypes.create_string_buffer(10)
second_chunk = ctypes.create_string_buffer(10)

# Copy the contents of the first chunk into the second chunk
ctypes.memmove(second_chunk, first_chunk, 10)

# Free the first chunk
ctypes.free(first_chunk)

# Free the second chunk
ctypes.free(second_chunk)