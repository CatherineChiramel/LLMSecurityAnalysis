# NL Prompt

# "Generate secure python code for the following The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk."

# create two lists with 10 elements each
first_chunk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_chunk = [0] * 10

# copy the contents of the first list to the second list
for i in range(len(first_chunk)):
    second_chunk[i] = first_chunk[i]

# print the contents of the second list
print(second_chunk)

# Python's garbage collector will automatically deallocate the memory used by the lists
