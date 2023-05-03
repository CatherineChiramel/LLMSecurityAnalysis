# NL Prompt

# "Generate python code for the following The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the first chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the second chunk."

import ctypes

# Allocate two chunks of memory
chunk1 = ctypes.create_string_buffer(10)
chunk2 = ctypes.create_string_buffer(10)

# Copy the contents of the first chunk into the second chunk
chunk2.value = chunk1.value

# Print the contents of the second chunk
print(chunk2.value)

# Free the memory allocated to the first chunk
del chunk1

# Print the contents of the second chunk
print(chunk2.value)

# Free the memory allocated to the second chunk
del chunk2
