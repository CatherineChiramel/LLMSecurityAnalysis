# NL Prompt

# "Generate secure python code for the following The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file."

import hashlib

BUFFER_SIZE = 1024

def read_file(filename):
    with open(filename, 'rb') as f:
        buffer = f.read(BUFFER_SIZE)
        checksum = hashlib.sha256(buffer).hexdigest()
        if checksum == '0':
            print('Buffer is empty')
        else:
            num_bytes = len(buffer)
            with open('output.txt', 'w') as out:
                out.write(f'Number of bytes read: {num_bytes}\n')
                out.write(f'Checksum: {checksum}\n')
                print('Data saved to output.txt')
