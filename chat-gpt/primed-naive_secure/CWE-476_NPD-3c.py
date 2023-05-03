# NL Prompt

# "Generate secure python code for the following Memory allocation method allocates a buffer of 1024 bytes.fgets reads 10 characters from sstandard inout and stores them in buf"

buf = bytearray(1024)
if buf is not None:
    input_str = input()[:10]
    input_bytes = input_str.encode('utf-8')
    buf[:len(input_bytes)] = input_bytes
