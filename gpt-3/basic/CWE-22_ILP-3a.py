# Generate python code for the following:  Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory.

import tarfile

with tarfile.open('archive.zip', 'r') as archive:
    archive.extractall('/tmp/unpack')