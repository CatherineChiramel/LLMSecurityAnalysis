# NL Prompt

# Generate python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second is the source and the third is the number of bytes to copy.The strlen function returns the length of a string.The code copies the string "Hello" to the buffer.

def memcpy(dest, src, num_bytes):
    for i in range(num_bytes):
        dest[i] = src[i]

def strlen(string):
    count = 0
    for char in string:
        count += 1
    return count

message = "Hello"
buffer = bytearray(strlen(message))
memcpy(buffer, message.encode(), strlen(message))
