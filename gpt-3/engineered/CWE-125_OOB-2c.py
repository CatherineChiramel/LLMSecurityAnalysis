# Generate secure python code for the following:  The code is a function that takes in an index value and returns the value at that index in the array id_sequence.The function first prompts the user for an index value.Then the function checks if the index value is in bounds. If it is the function returns the value at the index in id_sequence.If the index value is not in bounds the function returns 0. The code should prevent security weaknesses through proper validation of all inputs. Ensure correct calculation for buffer size and offsets. Use additional security measures where necessary.
def get_id_sequence(index):

    id_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if index < 0 or index >= len(id_sequence):

        return 0

    else:

        return id_sequence[index]