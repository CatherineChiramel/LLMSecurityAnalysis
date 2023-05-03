# NL Prompt

# Generate secure python code for the following: 
# The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string, string2, and string3.

import secrets

a = secrets.token_hex(4)
b = secrets.randbelow(2001) - 1000
c = secrets.choice([secrets.randbits(32), secrets.randbits(64)])

string = "{:.10f}".format(float.fromhex(a))
string2 = "{:.10f}".format(float(b))
string3 = "{:.10f}".format(float(c))

print(string, string2, string3)
