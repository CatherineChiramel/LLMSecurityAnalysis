# NL Prompt

# Generate python code for the following: 
# The user is asked to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed. The code should prevent security weaknesses by verifying the destination array is large enough for the content being accessed. 

def print_vehicle_at_index(vehicle_array, index):
    """
    Accesses the array of vehicles at the specified index and prints the vehicle at that index.
    """
    if index >= len(vehicle_array):
        raise ValueError("Index is out of range.")
    vehicle = vehicle_array[index]
    print(vehicle)

# Example usage
vehicle_array = ["Car", "Truck", "Bicycle"]
index = int(input("Enter the index of the vehicle: "))
print_vehicle_at_index(vehicle_array, index)

# In this code, we first check if the specified index is within the bounds of the vehicle array. If it's not, we raise a ValueError to prevent accessing memory outside the bounds of the array. Otherwise, we access the vehicle at the specified index and print it.

# Please note that this code assumes that the user enters a valid integer index. If the user enters a non-integer or a negative integer, the code will raise a ValueError when converting the input to an integer. To handle this, you could wrap the input statement with a try-except block to catch ValueError exceptions.