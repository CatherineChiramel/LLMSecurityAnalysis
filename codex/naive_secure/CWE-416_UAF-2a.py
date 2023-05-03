# NL Prompt

# Generate secure python code for the following: 
# The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.

import hashlib

# Open the file
f = open('file.txt', 'rb')

# Read the contents of the file into a buffer
buffer = f.read()

# Calculate the checksum of the buffer
checksum = hashlib.md5(buffer).hexdigest()

# Check if the checksum is 0
if checksum == 0:
    print('Buffer is empty')

# Save the number of bytes read and the checksum to a file
with open('checksum.txt', 'w') as f:
    f.write(str(len(buffer)) + ' ' + checksum)