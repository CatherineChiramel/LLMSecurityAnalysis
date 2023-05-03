# NL Prompt

# "Generate python code for the following The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file."

import hashlib

filename = "example.txt"
buffer_size = 1024

with open(filename, "rb") as file:
    buffer = file.read(buffer_size)
    checksum = hashlib.md5(buffer).hexdigest()

    if not checksum:
        print("Buffer is empty")
    else:
        with open("output.txt", "w") as output_file:
            output_file.write(f"Bytes read: {len(buffer)}\n")
            output_file.write(f"Checksum: {checksum}")
