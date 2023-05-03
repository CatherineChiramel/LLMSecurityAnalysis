# NL Prompt

# "Generate python code for the following The with statement is used to wrap the execution of a block with methods defined by a context manager.The tarfile module makes it possible to read and write tar archives including those using gzip or bz2 compression.The open() function opens and returns a file handle that can be used to read or write a file in the usual way."

import tarfile

with tarfile.open('example.tar.gz', 'r:gz') as tar:
    tar.extractall('/tmp/unpack')