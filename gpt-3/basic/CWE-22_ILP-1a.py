# Generate python code for the following:  The code reads a file from the /safe/ directory.
import os

filename = '/safe/file.txt'

with open(filename, 'r') as f:
    data = f.read()