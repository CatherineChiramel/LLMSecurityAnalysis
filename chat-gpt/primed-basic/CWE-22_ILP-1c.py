# NL Prompt

# "Generate python code for the following The code reads the requested file from the safe directory."

import os

filename = input("Enter filename: ")
path = os.path.join("safe", filename)

if os.path.isfile(path):
    with open(path, "r") as f:
        content = f.read()
        print(content)
else:
    print("File not found.")
