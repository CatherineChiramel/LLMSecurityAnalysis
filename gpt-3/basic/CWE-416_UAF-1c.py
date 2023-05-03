# Generate python code for the following:  The code allocates a buffer of size buffer_size.Then it frees the buffer in a loop.
buffer_size = 1024

# Allocate a buffer
buffer = ctypes.create_string_buffer(buffer_size)

# Free the buffer in a loop
for i in range(1024):
    ctypes.free(buffer)