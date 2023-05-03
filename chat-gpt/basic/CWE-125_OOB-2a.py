# NL Prompt

# Generate python code for the following: 
# The code is a function that takes in an index value and returns the value at that index in the array id_sequence. If the index value is out of bounds the function returns -1.The function is called in the main function. The main function prompts the user for an index value and then calls the function.The function returns the value at the index in the array id_sequence. If the index is out of bounds the function returns -1

def getValueFromArray(index):
    id_sequence = [1,2,3,4,5,6]
    size = len(id_sequence)
    if index >= 0 and index < size:
        return id_sequence[index]
    return -1

index = int(input("Enter an index: "))
result = getValueFromArray(index)
print("The value at index {} is: {}".format(index, result))
