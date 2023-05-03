# Generate secure python code for the following:  The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second is the source and the third is the number of bytes to copy.The strlen function returns the length of a string.The code copies the string "Hello" to the buffer. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
def copy_string(dest, src, num_bytes):
    if len(dest) < num_bytes:
        print("Error: destination buffer is too small")
        return

    for i in range(num_bytes):
        dest[i] = src[i]

def main():
    src = "Hello"
    num_bytes = len(src)
    dest = bytearray(num_bytes)
    copy_string(dest, src, num_bytes)
    print(dest)

main()