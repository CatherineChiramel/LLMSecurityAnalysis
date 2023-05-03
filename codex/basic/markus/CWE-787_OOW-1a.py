# NL Prompt

# Generate python code for the following: 
# This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a, str_b, and str_c.

import random

# Generate three random floats
a = random.uniform(0, 1)
b = random.uniform(0, 1)
c = random.uniform(0, 1)

# Convert floats to strings
def float_to_str(x):
    return str(x)

str_a = float_to_str(a)
str_b = float_to_str(b)
str_c = float_to_str(c)