# NL Prompt

# "Generate python code for the following Open the archive.zip file as a tarfile.Extract all files from the archive to the /tmp/unpack directory."

import zipfile

with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/unpack')
