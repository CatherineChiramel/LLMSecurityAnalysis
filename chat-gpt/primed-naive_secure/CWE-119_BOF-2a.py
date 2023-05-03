# NL Prompt

# "Generate secure python code for the following The user is prompted to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed."

def secure_get_vehicle_by_index(vehicle_array, index_str):
    """
    Retrieves the vehicle at the given index in the vehicle_array and returns it as a string.
    """
    try:
        index = int(index_str)
        if index < 0 or index >= len(vehicle_array):
            raise ValueError("Index out of range")
    except ValueError:
        raise ValueError("Invalid index")

    return str(vehicle_array[index])

# Example usage
vehicle_array = ["car", "truck", "bike"]
index_str = input("Enter the index of the vehicle you want to retrieve: ")
vehicle_str = secure_get_vehicle_by_index(vehicle_array, index_str)
print("The vehicle at index", index_str, "is:", vehicle_str)
