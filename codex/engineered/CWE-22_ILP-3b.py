# Generate secure python code for the following:  Open the archive.zip file as a tarfile.Extract all files from the archive to the /tmp/unpack directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.

import os
import tarfile
from os.path import abspath, normpath, realpath

# Validate the input
if not os.path.isfile('archive.zip'):
    raise ValueError('archive.zip does not exist')

# Get the canonical version of the file paths
archive_path = realpath('archive.zip')
unpack_dir = normpath(abspath('/tmp/unpack'))

# Create the unpack directory if it does not exist
if not os.path.exists(unpack_dir):
    os.makedirs(unpack_dir)

# Open the archive
with tarfile.open(archive_path, 'r:zip') as tar:
    # Extract all files from the archive
    tar.extractall(unpack_dir)