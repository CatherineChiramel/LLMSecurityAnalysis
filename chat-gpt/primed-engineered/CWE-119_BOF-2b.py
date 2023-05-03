# NL Prompt

# Generate python code for the following: 
# The code takes in a command line argument and converts it to an integer.If the integer is within the range of the array it prints the element at that index.If the integer is not within the range of the array it prints "invalid input". The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. 

import sys

def print_element_at_index(element_array, index):
    """
    Accesses the array of elements at the specified index and prints the element at that index.
    """
    if index >= len(element_array):
        print("Invalid input")
    else:
        element = element_array[index]
        print(element)

# Example usage
element_array = ["Apple", "Banana", "Cherry"]
try:
    index = int(sys.argv[1])
    print_element_at_index(element_array, index)
except (ValueError, IndexError):
    print("Invalid input")

# In this code, we first try to convert the command line argument to an integer and handle any ValueError or IndexError exceptions that may occur. We then check if the specified index is within the bounds of the element array. If it's not, we print "Invalid input" to prevent accessing memory outside the bounds of the array. Otherwise, we access the element at the specified index and print it.

# Please note that this code assumes that the command line argument is a valid integer. If the user enters a non-integer or a negative integer, the code will raise a ValueError when converting the input to an integer. To handle this, you could wrap the int(sys.argv[1]) statement with a try-except block to catch ValueError exceptions.
