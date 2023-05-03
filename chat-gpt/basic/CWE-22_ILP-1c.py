# NL Prompt

# Generate python code for the following: 
# The code reads the requested file from the safe directory.

import os

def read_file(file_name):
    file_path = os.path.join("safe", file_name)
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "The requested file was not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

requested_file = input("Enter the name of the file to read: ")
file_contents = read_file(requested_file)
print(file_contents)
