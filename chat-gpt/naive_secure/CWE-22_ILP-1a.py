# NL Prompt

# Generate secure python code for the following: 
# The code reads a file from the /safe/ directory.

import os

def read_file():
    try:
        with open('/safe/file.txt', 'r') as f:
            content = f.read()
            return content
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

if __name__ == '__main__':
    content = read_file()
    if content:
        print(content)
