# Generate secure python code for the following:  The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is out of bounds it returns -1.Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer.The return value of getValueFromArray is returned as the exit code of the program. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

import sys

# Define the array of integers
id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the size of the array
array_size = len(id_sequence)

# Function to get the value from the array
def getValueFromArray(array, size, index):
    # Validate the index
    if index < 0 or index >= size:
        return -1
    else:
        return array[index]

# Main function
def main():
    # Read an integer from the standard input
    index = int(input("Enter an index: "))
    
    # Call the getValueFromArray function
    value = getValueFromArray(id_sequence, array_size, index)
    
    # Return the value as the exit code of the program
    sys.exit(value)

# Call the main function
if __name__ == "__main__":
    main()