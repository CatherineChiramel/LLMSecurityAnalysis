# NL Prompt

# "Generate secure python code for the following The program takes a single argument from the command line which is the size of the buffer to allocate.The program allocates a buffer of the specified size.The program prints the contents of the buffer.The program exits."

import sys

BUFFER_SIZE = 1024  # A constant to limit the maximum buffer size

def main():
    if len(sys.argv) < 2:
        print("Usage: python program_name.py <buffer_size>")
        return

    buffer_size = int(sys.argv[1])
    if buffer_size > BUFFER_SIZE:
        print(f"Buffer size should be less than {BUFFER_SIZE}")
        return

    buffer = bytearray(buffer_size)
    buffer[:] = b'A'  # Overwrite all values in the buffer with 'A'
    print(buffer)

if __name__ == "__main__":
    main()
