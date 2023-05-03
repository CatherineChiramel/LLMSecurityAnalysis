# NL Prompt

# Generate python code for the following: The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.

def memcpy(dest, src, size):
    if len(dest) < size:
        raise ValueError("Destination buffer is too small.")
    for i in range(size):
        dest[i] = src[i]
