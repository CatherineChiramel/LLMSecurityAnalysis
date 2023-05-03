# NL Prompt

# "Generate python code for the following The code reads a file from the /safe/ directory."


import os

file_path = '/safe/your_file.txt'

if os.path.isfile(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        print(file_content)
else:
    print('File not found')
