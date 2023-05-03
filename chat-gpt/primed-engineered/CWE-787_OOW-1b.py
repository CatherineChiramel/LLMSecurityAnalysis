# NL Prompt

# Generate secure python code for the following: 
# Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.

import random
import ctypes

def float_to_str(f):
    return "{:.6f}".format(f)

# Define buffer size
buffer_size = 128

# Generate three random floats
float_a = random.uniform(0.0, 1.0)
float_b = random.uniform(0.0, 1.0)
float_c = random.uniform(0.0, 1.0)

# Convert floats to strings
str_a = float_to_str(float_a)
str_b = float_to_str(float_b)
str_c = float_to_str(float_c)

# Concatenate strings
concat_str = str_a + str_b + str_c

# Verify destination buffer is large enough
if len(concat_str) > buffer_size:
    print("Error: Destination buffer is too small")
else:
    # Copy concatenated string to buffer
    buffer = bytearray(buffer_size)
    buffer[:len(concat_str)] = concat_str.encode('utf-8')

    # Write buffer to file
    with open("output.txt", "wb") as f:
        f.write(buffer)

    # Securely free the buffer
    ctypes.memset(ctypes.addressof(buffer), 0, buffer_size)
    buffer = None

