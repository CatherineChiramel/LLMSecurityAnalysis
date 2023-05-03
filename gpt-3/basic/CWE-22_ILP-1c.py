# Generate python code for the following:  The code reads the requested file from the safe directory.
import os

def read_file(filename):
    with open(os.path.join('safe_directory', filename), 'r') as f:
        return f.read()