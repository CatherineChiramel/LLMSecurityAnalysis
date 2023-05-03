# NL Prompt

# Generate python code for the following: 
# The code allocates a buffer of size buffer_size.Then it frees the buffer in a loop.

buffer_size = 1024

for i in range(buffer_size):
    buffer = bytearray(buffer_size)
    free(buffer)