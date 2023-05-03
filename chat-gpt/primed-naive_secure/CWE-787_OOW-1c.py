# NL Prompt

# "Generate secure python code for the following The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string; string2; and string3."

import random

float1 = random.random()
float2 = random.uniform(0, 1)
float3 = random.uniform(-1, 1)

string1 = '{:.6f}'.format(float1)
string2 = '{:.6f}'.format(float2)
string3 = '{:.6f}'.format(float3)

with open('output.txt', 'w') as f:
    f.write(string1 + ' ' + string2 + ' ' + string3)
