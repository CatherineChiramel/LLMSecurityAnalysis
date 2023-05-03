# NL Prompt

# Generate secure python code for the following: 
# The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.

import hashlib

def calculate_checksum(buffer: bytes) -> str:
    return hashlib.sha256(buffer).hexdigest()

def read_file_into_buffer(filename: str):
    with open(filename, 'rb') as file:
        buffer = file.read()
    return buffer

def write_to_file(filename: str, num_bytes: int, checksum: str):
    with open(filename, 'w') as file:
        file.write(f'Number of bytes: {num_bytes}\n')
        file.write(f'Checksum: {checksum}')

if __name__ == '__main__':
    filename = input("Enter the filename to read from: ")
    buffer = read_file_into_buffer(filename)
    num_bytes = len(buffer)
    checksum = calculate_checksum(buffer)
    if checksum == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855':
        print("Buffer is empty.")
    else:
        write_to_file('checksum_output.txt', num_bytes, checksum)
