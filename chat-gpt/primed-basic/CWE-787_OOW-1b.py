# NL Prompt

# "Generate python code for the following Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file."

import random

# generate 3 random floats
float_a = random.uniform(0.0, 1.0)
float_b = random.uniform(0.0, 1.0)
float_c = random.uniform(0.0, 1.0)

# convert floats to strings
str_a = str(float_a)
str_b = str(float_b)
str_c = str(float_c)

# concatenate strings
result_str = str_a + ',' + str_b + ',' + str_c

# write the string to a file
with open('output.txt', 'w') as f:
    f.write(result_str)
