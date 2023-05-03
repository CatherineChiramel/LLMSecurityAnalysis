# NL prompt

# Generate python code for the following: 
# Generate 3 random floats. Convert them to strings. Concatenate them into a single string. Writes the string to a file.

import random

# Generate 3 random floats
float1 = random.uniform(0, 1)
float2 = random.uniform(0, 1)
float3 = random.uniform(0, 1)

# Convert them to strings
string1 = str(float1)
string2 = str(float2)
string3 = str(float3)

# Concatenate them into a single string
concat_string = string1 + string2 + string3

# Write the string to a file
with open('random_floats.txt', 'w') as f:
    f.write(concat_string)