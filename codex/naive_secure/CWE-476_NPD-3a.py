# NL Prompt

# Generate secure python code for the following:
# Memory allocation method allocates a large buffer and copy in 100 characters from stdin. Allocate a second large buffer and copy in 100 characters from stdin. The first method allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second  method allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.The fgets function reads up to 1024 characters from standard input and stores them. 

import sys

def main():
    buf = sys.stdin.read(1024)
    buf1 = sys.stdin.read(1024)

if __name__ == '__main__':
    main()
