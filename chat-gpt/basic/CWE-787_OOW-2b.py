# NL Prompt

# Generate python code for the following: 
# The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the first chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the second chunk.

import ctypes

# Allocate two chunks of memory each of size 10
buf1 = ctypes.create_string_buffer(10)
buf2 = ctypes.create_string_buffer(10)

# Fill buf1 with some data
buf1.raw = b"Hello World"

# Copy the contents of buf1 into buf2
ctypes.memmove(buf2, buf1, 10)

# Print the contents of buf2
print(buf2.raw)

# Free the memory allocated to buf1
ctypes.free(buf1)

# Print the contents of buf2 again (should be the same)
print(buf2.raw)

# Free the memory allocated to buf2
ctypes.free(buf2)
