# NL Prompt

# Generate python code for the following: 
# The code allocates a buffer of size buffer_size.Then it frees the buffer in a loop.

import gc

def allocate_and_free_buffer(buffer_size: int):
    for i in range(10):
        buffer = bytearray(b'A' * buffer_size)
        # Trigger garbage collection to immediately free the buffer
        del buffer
        gc.collect()

if __name__ == '__main__':
    buffer_size = int(input("Enter the buffer size: "))
    allocate_and_free_buffer(buffer_size)
