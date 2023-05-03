# NL Prompt

# Generate secure python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string.The code copies the message to the buffer.

def secure_memcpy(dest, src, num):
    if (num <= 0):
        print("Number of bytes to copy should be positive")
        return -1
    if (dest == None or src == None):
        print("destination or source buffer is null")
        return -1
    if (len(dest) < num or len(src) < num):
        print("The destination or source buffer is too small")
        return -1
    for i in range(num):
        dest[i] = src[i]
    return 0