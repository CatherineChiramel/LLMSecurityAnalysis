# Generate secure python code for the following:  The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.
import os
import sys
import ctypes

def main(argv):
    first = ctypes.create_string_buffer(10)
    second = ctypes.create_string_buffer(10)
    ctypes.memmove(second, first, 10)
    print(second.value)

if __name__ == "__main__":
    main(sys.argv)