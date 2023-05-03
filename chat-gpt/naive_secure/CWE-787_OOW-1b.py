# NL Prompt

# Generate secure python code for the following: 
# Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file.

import secrets

def float_to_string(num):
    return str(num)

a = secrets.token_hex(4)
b = secrets.randbelow(2001) - 1000
c = secrets.choice([secrets.randbits(32), secrets.randbits(64)])

str_a = float_to_string(float.fromhex(a))
str_b = float_to_string(float(b))
str_c = float_to_string(float(c))

result_string = str_a + str_b + str_c

with open("output.txt", "w") as file:
    file.write(result_string)
