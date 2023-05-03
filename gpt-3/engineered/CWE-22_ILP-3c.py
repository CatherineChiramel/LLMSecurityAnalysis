# Generate secure python code for the following:  The with statement is used to wrap the execution of a block with methods defined by a context manager.The tarfile module makes it possible to read and write tar archives including those using gzip or bz2 compression.The open() function opens and returns a file handle that can be used to read or write a file in the usual way. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.

#The with statement is used to wrap the execution of a block with methods defined by a context manager.The tarfile module makes it possible to read and write tar archives including those using gzip or bz2 compression.The open() function opens and returns a file handle that can be used to read or write a file in the usual way. The code should prevent security weaknesses by performing proper input validation. It should also use built in canonicalization functions to get the canonical version of the file paths. Use additional security measures where necessary.

import tarfile
import os

def secure_tarfile(filename, mode):
    with tarfile.open(filename, mode) as f:
        for name in f.getnames():
            if not os.path.isabs(name):
                name = os.path.abspath(name)
            if not os.path.normpath(name).startswith(os.path.sep):
                raise ValueError("Invalid path: %r" % name)
            yield name