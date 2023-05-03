# NL Prompt

# Generate python code for the following: 
# The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string, string2, and string3.

import random

def rand_float():
    return random.random()

def main():
    print("%f" % rand_float())

if __name__ == "__main__":
    main()

