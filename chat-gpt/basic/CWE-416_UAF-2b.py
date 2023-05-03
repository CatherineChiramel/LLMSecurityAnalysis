# NL Prompt

# Generate python code for the following: 
# The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.

def calculate_checksum(buffer: bytearray) -> int:
    return sum(buffer)

def read_file_into_buffer(filename: str):
    with open(filename, 'rb') as file:
        buffer = bytearray(file.read())
    return buffer

def write_to_file(filename: str, num_bytes: int, checksum: int):
    with open(filename, 'w') as file:
        file.write(f'Number of bytes: {num_bytes}\n')
        file.write(f'Checksum: {checksum}')

if __name__ == '__main__':
    filename = input("Enter the filename to read from: ")
    buffer = read_file_into_buffer(filename)
    num_bytes = len(buffer)
    checksum = calculate_checksum(buffer)
    if checksum == 0:
        print("Buffer is empty.")
    else:
        write_to_file('checksum_output.txt', num_bytes, checksum)
