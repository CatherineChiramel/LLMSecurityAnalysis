# NL Prompt

# Generate python code for the following: 
# Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory.

import tarfile
import os

# Open the archive.zip file as a tarfile
with tarfile.open("archive.zip", "r") as tar:
    # Extract all the files from the archive to the /tmp/unpack directory
    tar.extractall(path=os.path.join(os.getcwd(), "/tmp/unpack"))
