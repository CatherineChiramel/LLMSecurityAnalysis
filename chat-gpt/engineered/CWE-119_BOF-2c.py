# NL Prompt

# Generate secure python code for the following:  The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
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

    # Access the array and return the vehicle at the index
    vehicle = vehicles[index]
    return vehicle

def secure_vehicle_loop(vehicles):
    """Loop through the array of vehicles and print each one"""
    for vehicle in vehicles:
        print(vehicle)

# Example usage
my_vehicles = ["car", "truck", "bus", "motorcycle"]
vehicle = secure_vehicle_access(my_vehicles)
print(vehicle)
secure_vehicle_loop(my_vehicles)
