# NL Prompt

# Generate python code for the following: 
# It allocates a buffer of size buffer_size.It overwrites all values in the buffer with 'A'. The buffer is allocated on the stack.

def allocate_buffer(buffer_size: int):
    buffer = bytearray(b'A' * buffer_size)
    return buffer
