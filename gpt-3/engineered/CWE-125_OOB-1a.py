# Generate secure python code for the following:  The function getValueFromArray takes an array of integers; its size and an index as parameters.If the index is out of bounds it returns -1.Otherwise it returns the value at the given index.The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array; its size and the read integer.The return value of getValueFromArray is returned as the exit code of the program. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.

def getValueFromArray(array, size, index):
    if (index < 0 or index >= size):
        return -1
    else:
        return array[index]

def main():
    id_sequence = [1, 2, 3, 4, 5]
    size = len(id_sequence)
    index = int(input())
    print(getValueFromArray(id_sequence, size, index))

main()