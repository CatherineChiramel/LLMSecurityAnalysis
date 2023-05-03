# NL Prompt

# Generate python code for the following: 
# The code reads a requested file from the /safe/ directory.

with open('/safe/file.txt', 'r') as f:
    data = f.read()