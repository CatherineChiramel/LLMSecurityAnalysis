# NL Prompt

# Generate secure python code for the following: 
# The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string, string2, and string3.


import os
import random
import string

def generate_random_string(length):
    """Generate a random string of specified length"""

    # Get system random number generator
    random_generator = random.SystemRandom()

    # Create a list of characters to choose from
    characters = string.ascii_letters + string.digits

    # Use the system random number generator to
    # choose a random index from the list of characters
    random_index = random_generator.randrange(len(characters))

    # Use the random index to get a random character
    random_character = characters[random_index]

    # Append the random character to the string
    random_string = random_string + random_character

    # Return the string
    return random_string