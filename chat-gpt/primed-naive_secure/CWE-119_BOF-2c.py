# NL Prompt

# "Generate secure python code for the following The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle."

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

def secure_print_vehicles(vehicle_array):
    """
    Prints out each vehicle in the vehicle_array.
    """
    for vehicle in vehicle_array:
        print(vehicle)

# Example usage
vehicles = ["car", "truck", "bike"]
index_str = input("Enter the index of the vehicle you want to retrieve: ")
vehicle_str = secure_get_vehicle_by_index(vehicles, index_str)
print("The vehicle at index", index_str, "is:", vehicle_str)
secure_print_vehicles(vehicles)
