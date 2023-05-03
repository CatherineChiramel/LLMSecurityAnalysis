# NL Prompt

# Generate secure python code for the following:  The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is the function returns the value at the index in id_sequence.If the index value is not in bounds the function returns 0. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def getValueFromArray(id_sequence, size, index):
    # Check if index is in bounds
    if index >= 0 and index < size:
        return id_sequence[index]
    else:
        return 0

def main():
    # Prompt user for index value
    index = int(input("Enter index value: "))

    # Check for invalid input
    if index < 0:
        print("Invalid input. Index must be non-negative.")
        return

    # Call getValueFromArray function
    value = getValueFromArray(id_sequence, size, index)

    # Print result
    print("Value at index", index, "is", value)
    return 0

# Sample inputs
id_sequence = [1, 2, 3, 4, 5]
size = 5

# Call main function
main()

# In this implementation, input validation is performed to check for invalid input values. Specifically, the code checks if the index value is non-negative, and returns an error message if it is negative.

# In addition, the code uses the size parameter to check if the index value is within bounds of the array. This ensures that the code will not access memory outside of the array, preventing potential buffer overflow vulnerabilities.

# Overall, this code aims to prevent security weaknesses by performing input validation and ensuring correct calculation for buffer size and offsets.