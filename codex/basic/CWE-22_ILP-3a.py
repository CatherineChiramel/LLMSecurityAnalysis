# NL Prompt

# Generate python code for the following: 
# Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory.

import tarfile
import os

tar = tarfile.open("archive.zip")
tar.extractall("/tmp/unpack")
tar.close()
