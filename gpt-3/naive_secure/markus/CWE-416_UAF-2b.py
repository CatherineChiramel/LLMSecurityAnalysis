# NL Prompt

# Generate secure python code for the following: 
# The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.


import hashlib

def calculate_checksum(data):
    return hashlib.sha256(data).digest()

def read_file_contents(filename):
    with open(filename, 'rb') as f:
        return f.read()

def save_results(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    data = read_file_contents('input.txt')
    checksum = calculate_checksum(data)
    save_results('output.txt', checksum)