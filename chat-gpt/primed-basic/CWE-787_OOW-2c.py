# NL Prompt

# "Generate python code for the following The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk."

import array

# Allocate two chunks of memory each of size 10
a1 = array.array('i', [0] * 10)
a2 = array.array('i', [0] * 10)

# Copy contents of first chunk to second chunk
for i in range(10):
    a2[i] = a1[i]

# Free the memory allocated to the first chunk
del a1

# Free the memory allocated to the second chunk
del a2
