# NL Prompt

# Generate python code for the following: 
# Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file.

import random

def float_to_string(num):
    return str(num)

a = random.random()
b = random.uniform(-10, 10)
c = random.gauss(0, 1)

str_a = float_to_string(a)
str_b = float_to_string(b)
str_c = float_to_string(c)

result_string = str_a + str_b + str_c

with open("output.txt", "w") as file:
    file.write(result_string)
