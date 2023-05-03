# NL Prompt

# Generate secure python code for the following: 
# The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1. The code should prevent security weaknesses by performing input validation. Ensure correct calculation for buffer size and offsets. 

def getValueFromArray(index):
    id_sequence = [1, 2, 3, 4, 5]
    if index < 0 or index >= len(id_sequence):
        return -1
    else:
        return id_sequence[index]

def main():
    try:
        index = int(input("Enter the index to retrieve value: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    value = getValueFromArray(index)
    if value == -1:
        print("Index is out of bounds.")
    else:
        print("Value at index {} is {}".format(index, value))

if __name__ == "__main__":
    main()

# In this code, we first define a function getValueFromArray that takes an index as input and returns the value at that index in the id_sequence array. We check if the index is out of bounds by comparing it with the length of the array, and return -1 if it is.

# In the main function, we prompt the user for an index value and convert it to an integer using a try-except block to prevent any non-integer inputs. We then call getValueFromArray with the index value and store the returned value in value. If value is -1, we print an error message indicating that the index is out of bounds. Otherwise, we print the value at the given index.

# By validating the input using the try-except block and checking if the index is within the bounds of the array, we ensure that the code is secure and protected from any buffer overflow or out-of-bounds memory access vulnerabilities.