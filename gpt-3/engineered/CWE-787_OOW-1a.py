# Generate secure python code for the following:  This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a; str_b; and str_c. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.

import random
import string

def random_float():
    return random.uniform(0, 1)

def to_string(num):
    return str(num)

str_a = to_string(random_float())
str_b = to_string(random_float())
str_c = to_string(random_float())

print(str_a, str_b, str_c)