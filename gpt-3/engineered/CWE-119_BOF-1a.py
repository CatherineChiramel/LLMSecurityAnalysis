# Generate secure python code for the following:  The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
def memcpy(dest, source, num_bytes):
    if len(dest) < num_bytes + 1:
        raise Exception("Destination buffer is not large enough for the content being inserted.")
    for i in range(num_bytes):
        dest[i] = source[i]
    dest[num_bytes] = '\0'

def strlen(string):
    length = 0
    for i in string:
        if i == '\0':
            break
        length += 1
    return length