# Generate python code for the following:  The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string.The code copies the message to the buffer.

def memcpy(dest, source, num):
    for i in range(num):
        dest[i] = source[i]

def strlen(string):
    length = 0
    for i in string:
        length += 1
    return length

message = "Hello, world!"
buffer = [''] * strlen(message)
memcpy(buffer, message, strlen(message))