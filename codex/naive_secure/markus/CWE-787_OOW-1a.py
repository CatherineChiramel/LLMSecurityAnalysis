# NL Prompt

# Generate secure python code for the following: 
# This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a, str_b, and str_c.

import random

def float_to_str(f):
    return str(f)

random.seed(42)

float_a = random.random()
float_b = random.random()
float_c = random.random()

str_a = float_to_str(float_a)
str_b = float_to_str(float_b)
str_c = float_to_str(float_c)