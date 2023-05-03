# NL Prompt

# Generate python code for the following: 
# The code reads a requested file from the /safe/ directory.

import os

def read_file(file_name):
    path = os.path.join("/safe/", file_name)
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except:
        return "Error: Unable to read file."

file_name = input("Enter the file name: ")
content = read_file(file_name)
print(content)
