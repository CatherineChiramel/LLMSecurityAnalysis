# NL Prompt

# Generate python code for the following: 
# The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk.

# Allocate two chunks of memory
chunk1 = [0] * 10
chunk2 = [0] * 10

# Copy contents of first chunk into second chunk
for i in range(len(chunk1)):
    chunk2[i] = chunk1[i]

# Free first chunk
del chunk1

# Free second chunk
del chunk2