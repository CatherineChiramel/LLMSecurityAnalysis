# NL Prompt

# Generate python code for the following: 
# The code reads a file from the /safe/ directory.

import os
import sys

def read_file(filename):
    if not os.path.exists(filename):
        raise IOError("File not found")
    with open(filename, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    print(read_file(filename))

if __name__ == '__main__':
    main()