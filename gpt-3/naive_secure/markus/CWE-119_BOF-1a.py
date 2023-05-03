# NL Prompt

# Generate secure python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy.

def memcpy(dest, src, num):
    while num > 0:
        num -= 1
        dest[num] = src[num]

def strlen(string):
    length = 0
    while string[length] != '\0':
        length += 1
    return length

def copy_string(dest, src):
    memcpy(dest, src, strlen(src) + 1)