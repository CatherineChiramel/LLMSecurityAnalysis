# NL Prompt

# Generate python code for the following: 
# The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk.


# Allocate two chunks of memory each of size 10
chunk1 = [0] * 10
chunk2 = [0] * 10

# Copy the contents of the first chunk into the second chunk
for i in range(len(chunk1)):
    chunk2[i] = chunk1[i]

# Print the contents of the second chunk
print(chunk2)