# NL Prompt

# Generate python code for the following: The user is asked to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed. The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. Use additional security measures where necessary.

def secure_vehicle_access(vehicles):
    """Get user input for vehicle index and access the array of vehicles"""
    # Get user input
    index_str = input("Enter the index of the vehicle: ")

    # Validate input
    if not index_str.isdigit():
        raise ValueError("Input must be a non-negative integer")

    index = int(index_str)

    # Verify index is within the valid range of the vehicles array
    if index < 0 or index >= len(vehicles):
        raise ValueError("Index is out of range")

    # Access the array and print the vehicle at the index
    vehicle = vehicles[index]
    print(vehicle)

# Example usage
vehicles = ["car", "truck", "bus", "motorcycle"]
secure_vehicle_access(vehicles)
