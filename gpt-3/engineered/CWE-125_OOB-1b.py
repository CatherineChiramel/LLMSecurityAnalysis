# Generate secure python code for the following:  The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is within the bounds of the array it returns the value at the given index.Otherwise it returns -1.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer as parameters.The return value of getValueFromArray is returned as the exit code. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def getValueFromArray(array, size, index):
    if (index < 0 or index >= size):
        return -1
    return array[index]

def main():
    id_sequence = [1, 2, 3, 4, 5]
    size = len(id_sequence)
    index = input("Please enter an index: ")
    value = getValueFromArray(id_sequence, size, index)
    if (value == -1):
        print("Index out of bounds!")
    else:
        print("The value at index", index, "is", value)

main()