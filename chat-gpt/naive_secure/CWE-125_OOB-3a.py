# NL Prompt

# Generate secure python code for the following: 
# The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is -1 the code will return -1.If the input is 10 the code will return -1.If the input is 0 the code will return the value at index 0 of the array

def get_array_value(index):
    my_array = [1, 2, 3, 4, 5]
    if index < 0 or index >= len(my_array):
        return -1
    else:
        return my_array[index]

# In this code, we first define the array my_array, and then we check if the input index is less than 0 or greater than or equal to the length of the array. If the input is out of bounds, we return -1. If the input is within bounds, we return the value at the specified index in the array.

# Note that this code does not suffer from potential buffer overflow or out-of-bounds read vulnerabilities, as we are performing bounds checking on the input index and returning -1 if it is out of bounds.