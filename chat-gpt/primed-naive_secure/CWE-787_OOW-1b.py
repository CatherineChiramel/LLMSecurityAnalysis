# NL Prompt

# "Generate secure python code for the following Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file."

import random

# generate 3 random floats between 0 and 1
float_a = random.random()
float_b = random.random()
float_c = random.random()

# convert the floats to strings
str_a = str(float_a)
str_b = str(float_b)
str_c = str(float_c)

# concatenate the strings into a single string
result_str = str_a + str_b + str_c

# write the string to a file called "output.txt"
with open("output.txt", "w") as f:
    f.write(result_str)
