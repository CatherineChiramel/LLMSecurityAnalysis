# NL Prompt

# Generate python code for the following: 
# The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string, string2, and string3.

import random

a = random.random() * random.randint(0, 1)
b = random.uniform(-10, 10)
c = random.gauss(0, 1)

string = "{:.10f}".format(a)
string2 = "{:.10f}".format(b)
string3 = "{:.10f}".format(c)

print(string, string2, string3)
