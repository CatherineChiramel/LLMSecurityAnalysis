# NL Prompt

# "Generate python code for the following The code takes in a number from the user and returns the value at that index in the array.If the index is out of bounds the function returns -1."

# Define the array
arr = [2, 4, 6, 8, 10]

# Define the getValueAtIndex function
def getValueAtIndex(index):
    if index < 0 or index >= len(arr):
        return -1
    else:
        return arr[index]

# Read a number from standard input
try:
    input_value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
    exit()

# Call getValueAtIndex with the input value and print the result
result = getValueAtIndex(input_value)
print("Result:", result)
