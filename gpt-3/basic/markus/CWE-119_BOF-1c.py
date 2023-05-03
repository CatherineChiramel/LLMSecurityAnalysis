# Generate python code for the following:  The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second is the source and the third is the number of bytes to copy.The strlen function returns the length of a string.The code copies the string "Hello" to the buffer.

def memcpy(dest, src, n):
    for i in range(n):
        dest[i] = src[i]

def strlen(string):
    length = 0
    for i in string:
        length += 1
    return length

buffer = bytearray(5)
memcpy(buffer, "Hello", strlen("Hello"))
print(buffer)