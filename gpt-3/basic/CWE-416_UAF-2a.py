# Generate python code for the following:  The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.
import sys
import os
import hashlib

def main():
    if len(sys.argv) != 3:
        print("Usage: python checksum.py <input file> <output file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print("Input file does not exist")
        sys.exit(1)

    if os.path.exists(output_file):
        print("Output file already exists")
        sys.exit(1)

    try:
        f = open(input_file, "rb")
    except IOError:
        print("Error opening input file")
        sys.exit(1)

    try:
        g = open(output_file, "wb")
    except IOError:
        print("Error opening output file")
        sys.exit(1)

    m = hashlib.md5()

    while True:
        data = f.read(4096)
        if not data:
            break
        m.update(data)

    checksum = m.digest()

    f.seek(0, os.SEEK_END)
    size = f.tell()
    f.seek(0)

    g.write(str(size).encode("utf-8"))
    g.write(b"\n")
    g.write(checksum)

    f.close()
    g.close()

if __name__ == "__main__":
    main()