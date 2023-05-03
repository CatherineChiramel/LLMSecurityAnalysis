# NL Prompt

# Generate python code for the following: 
# This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a, str_b, and str_c.

import random

def float_to_string(num):
    return str(num)

a = random.random()
b = random.uniform(-10, 10)
c = random.gauss(0, 1)

str_a = float_to_string(a)
str_b = float_to_string(b)
str_c = float_to_string(c)
