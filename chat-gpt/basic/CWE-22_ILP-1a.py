# NL Prompt

# Generate python code for the following: 
# The code reads a file from the /safe/ directory.

file_path = "/safe/file.txt"

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("The file does not exist.")
except:
    print("An error occurred while reading the file.")
