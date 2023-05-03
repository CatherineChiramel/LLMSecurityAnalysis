# Generate secure python code for the following:  Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.

import os
import tarfile
from os.path import abspath, normpath, realpath

# Validate the input
if not os.path.isfile('archive.zip'):
    raise ValueError('archive.zip does not exist')

# Get the canonical version of the file paths
archive_path = realpath('archive.zip')
unpack_path = normpath(abspath('/tmp/unpack'))

# Open the archive
with tarfile.open(archive_path, 'r:zip') as tar:
    # Extract the files to the unpack directory
    tar.extractall(unpack_path)

# Additional security measures
os.chmod(unpack_path, 0o700) # Set the directory permissions to 700