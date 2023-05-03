# Generate python code for the following:  This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a; str_b; and str_c.
import random

def random_float():
  return random.uniform(0, 1)

str_a = str(random_float())
str_b = str(random_float())
str_c = str(random_float())