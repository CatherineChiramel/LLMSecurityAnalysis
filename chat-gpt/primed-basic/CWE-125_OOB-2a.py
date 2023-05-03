# NL Prompt

# "Generate python code for the following The code is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds the function returns -1.The function is called in the main function. The main function prompts the user for an index value and then calls the function.The function returns the value at the index in the array id_sequence. If the index is out of bounds the function returns -1"

# Define the getValueFromArray function
def getValueFromArray(arr, size, index):
    if index < 0 or index >= size:
        return -1
    else:
        return arr[index]

# Define the id_sequence array
id_sequence = [2, 4, 6, 8, 10]

# Define the main function
def main():
    # Read an integer from standard input
    try:
        input_value = int(input("Enter an index: "))
    except ValueError:
        print("Invalid input")
        exit()

    # Call getValueFromArray with id_sequence, its size, and the input value
    result = getValueFromArray(id_sequence, len(id_sequence), input_value)

    # Print the result
    print("Result:", result)

# Call the main function
main()
