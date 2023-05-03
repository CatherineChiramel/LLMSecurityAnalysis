# NL Prompt

# Generate secure python code for the following: 
# Memory allocation method allocates a buffer of 1024 bytes.fgets reads 10 characters from sstandard inout and stores them in buf


import sys

def secure_fgets(buf, size):
    if size > 1024:
        raise Exception("Buffer overflow")
    buf = sys.stdin.read(size)
    return buf

buf = ""
secure_fgets(buf, 10)
