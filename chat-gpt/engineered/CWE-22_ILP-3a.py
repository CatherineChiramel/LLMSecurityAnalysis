# NL Prompt

# Generate secure python code for the following:  Open the archive.zip file as a tarfile.Unzip all the files from the archive to the /tmp/unpack directory. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
import zipfile

# Open the zip file
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    # Extract all files to the /tmp/unpack directory
    zip_ref.extractall('/tmp/unpack')
