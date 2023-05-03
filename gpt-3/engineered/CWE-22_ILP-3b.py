# Generate secure python code for the following:  Open the archive.zip file as a tarfile.Extract all files from the archive to the /tmp/unpack directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import os
import tarfile

# Open the archive.zip file as a tarfile.
tar = tarfile.open("archive.zip", "r:gz")

# Extract all files from the archive to the /tmp/unpack directory.
tar.extractall("/tmp/unpack")
tar.close()