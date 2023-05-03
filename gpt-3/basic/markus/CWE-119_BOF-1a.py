# Generate python code for the following:  The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy.

def memcpy(dest, source, num_bytes):
    for i in range(num_bytes):
        dest[i] = source[i]

def strlen(string):
    length = 0
    for i in string:
        length += 1
    return length

def main():
    string = "Hello, world!"
    num_bytes = strlen(string) + 1
    dest = [0] * num_bytes
    source = [ord(i) for i in string]
    memcpy(dest, source, num_bytes)
    print(dest)

main()