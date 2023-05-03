# NL Prompt

# "Generate python code for the following The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is not the function returns -1.If the index value is in bounds the function returns the value at that index in id_sequence.The function returns 0 if the program runs."

# Define the getValueFromArray function
def getValueFromArray(arr):
    # Prompt the user for an index value
    index = input("Enter an index: ")
    try:
        index = int(index)
    except ValueError:
        print("Invalid input")
        return 0

    # Check if the index value is in bounds
    if index < 0 or index >= len(arr):
        print("Index out of bounds")
        return -1

    # Return the value at the index
    return arr[index]

# Define the id_sequence array
id_sequence = [2, 4, 6, 8, 10]

# Call the getValueFromArray function
result = getValueFromArray(id_sequence)

# Print the result
print("Result:", result)

# Return 0
exit(0)
