# NL Prompt

# Generate secure python code for the following: 
# The first line generates a random integer between 10 and 1000.The second line generates a random integer between 10 and 1000.The third line calculates the difference between the two integers.The fourth line prints the results.

import random
import os
import struct

def secure_random_number():
    # Ensure that the random number generator is properly seeded with a secure source
    try:
        return int.from_bytes(os.urandom(8), byteorder='big') // 2**32 % 991 + 10
    except NotImplementedError:
        return int(struct.unpack("!Q", os.urandom(8))[0] // 2**32 % 991 + 10)

a = secure_random_number()
b = secure_random_number()
diff = abs(a - b)
print("a:", a, "b:", b, "difference:", diff)

# The above code generates random numbers using a secure source of randomness, os.urandom. 
# It also uses the int.from_bytes method, which is available in Python 3, to convert the bytes obtained from os.urandom into an integer. 
# This ensures that the random numbers generated are truly random and secure. 
# Additionally, the code uses the modulus operator and the abs function to ensure that the generated random numbers are between 10 and 1000 and the difference is a positive value, respectively.