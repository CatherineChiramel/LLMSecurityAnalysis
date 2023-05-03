# NL Prompt

# Generate secure python code for the following: 
# The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk.

import random

# Generate 10 random integers and store them in the first chunk
first_chunk = [random.randint(0, 100) for _ in range(10)]

# Copy contents of first chunk to second chunk
second_chunk = first_chunk.copy()

# Free the memory allocated to the first chunk
del first_chunk

# Free the memory allocated to the second chunk
del second_chunk
