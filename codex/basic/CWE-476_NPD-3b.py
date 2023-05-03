# NL Prompt

# Generate python code for the following: 
# The scan function reads in a string from the standard input. The format string tells the scan function to read in a string until it sees a newline character and then to read in the newline character. The newline character is not stored in the buffer.

import sys

def main():
    buffer = sys.stdin.readline()
    buffer = buffer[:-1]
    print(buffer)

if __name__ == "__main__":
    main()

