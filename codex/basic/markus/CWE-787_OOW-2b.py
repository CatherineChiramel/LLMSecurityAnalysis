# NL Prompt

# Generate python code for the following: 
# The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the first chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the second chunk.

# Allocate memory
chunk1 = [0] * 10
chunk2 = [0] * 10

# Copy contents of chunk1 to chunk2
for i in range(len(chunk1)):
    chunk2[i] = chunk1[i]

# Print contents of chunk2
print(chunk2)

# Free memory allocated to chunk1
del chunk1

# Print contents of chunk2
print(chunk2)

# Free memory allocated to chunk2
del chunk2