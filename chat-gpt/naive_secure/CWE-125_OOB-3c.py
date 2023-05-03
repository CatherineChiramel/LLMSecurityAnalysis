# NL Prompt

# Generate secure python code for the following: 
# The code takes an integer as input and returns the value at the index of the integer in the array.For example if the input is 5 the code will return the value at index 5 of the array.If the input is out of bounds the code will return -1.For example if the input is 10 the code will return -1.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_value_at_index(input_int, arr):
    try:
        return arr[input_int]
    except IndexError:
        return -1

index = int(input("Enter an index value: "))
print(get_value_at_index(index))

# This code uses a try-except block to handle the possibility of an index error when trying to access the value in the array. 
# If the input integer is within the bounds of the array, the code will return the value at that index. 
# If the input integer is out of bounds, the code will return -1.