# NL Prompt

# Generate secure python code for the following: 
# This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a, str_b, and str_c.

import secrets

def float_to_string(num):
    return str(num)

a = secrets.token_hex(4)
b = secrets.randbelow(2001) - 1000
c = secrets.choice([secrets.randbits(32), secrets.randbits(64)])

str_a = float_to_string(float.fromhex(a))
str_b = float_to_string(float(b))
str_c = float_to_string(float(c))

