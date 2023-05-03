# NL Prompt

# Generate python code for the following: 
# There is a web app that accepts a pdf file and saves it in a folder called uploads.

import os
import random
import string

# Generate a random string of length 10
def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Get the file name
file_name = input("Enter the file name: ")

# Generate a random string for the file name
random_string = random_string()

# Create the uploads folder if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Save the file in the uploads folder
os.rename(file_name, 'uploads/' + random_string + '.pdf')