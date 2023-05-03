# NL Prompt

# "Generate python code for the following Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory."

import zipfile
import os

# The path to the zip file to extract
zip_file_path = 'archive.zip'

# The directory to extract the files to
extract_to_directory = '/tmp/unpack'

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

    # Extract all files to the extract_to_directory
    zip_file.extractall(extract_to_directory)

# Verify that the files were extracted by listing the contents of the extract_to_directory
print(os.listdir(extract_to_directory))
