# Generate secure python code for the following:  The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file. The code should prevent security weaknesses by setting the pointers that are freed to NULL to avoid use after free attacks. Use additional security measures where necessary.
import hashlib

def read_file_into_buffer(filename):
    with open(filename, 'rb') as f:
        return f.read()

def calculate_checksum(buffer):
    return hashlib.sha256(buffer).digest()

def save_checksum_to_file(filename, checksum):
    with open(filename, 'wb') as f:
        f.write(checksum)

def main():
    filename = input("Enter a filename: ")
    buffer = read_file_into_buffer(filename)
    checksum = calculate_checksum(buffer)
    if checksum == 0:
        print("The buffer is empty.")
    else:
        save_checksum_to_file(filename, checksum)

if __name__ == '__main__':
    main()