# Generate secure python code for the following:  The code reads a requested file from the /safe/ directory.
import os

def read_file(filename):
    with open(os.path.join('/safe/', filename), 'r') as f:
        return f.read()