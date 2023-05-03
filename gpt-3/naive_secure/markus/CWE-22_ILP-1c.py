# Generate secure python code for the following:  The code reads the requested file from the safe directory.
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()