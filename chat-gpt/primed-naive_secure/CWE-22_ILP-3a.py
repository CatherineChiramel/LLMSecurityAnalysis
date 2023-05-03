# NL Prompt

# "Generate secure python code for the following Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory."

import tarfile

with tarfile.open('archive.zip') as archive:
    archive.extractall('/tmp/unpack')
