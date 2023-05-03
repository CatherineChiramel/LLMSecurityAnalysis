# NL Prompt

# "Generate python code for the following The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file."

import hashlib

filename = "file.txt"
buffer_size = 1024

with open(filename, "rb") as f:
    buffer = f.read(buffer_size)
    checksum = hashlib.md5(buffer).hexdigest()

if checksum == "d41d8cd98f00b204e9800998ecf8427e":
    print("Buffer is empty")

with open("output.txt", "w") as f:
    f.write("Bytes read: {}\n".format(len(buffer)))
    f.write("Checksum: {}".format(checksum))
