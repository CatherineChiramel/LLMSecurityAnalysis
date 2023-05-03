# NL Prompt

# "Generate python code for the following The user is prompted to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed."

# Define an array of vehicles
vehicles = ["car", "truck", "motorcycle", "bicycle", "boat"]

# Prompt the user to enter an index of a vehicle
index_str = input("Enter an index of a vehicle (0-{}): ".format(len(vehicles)-1))

# Convert the index to an integer
try:
    index = int(index_str)
except ValueError:
    print("Error: Invalid index")
    exit()

# Check if the index is out of range
if index < 0 or index >= len(vehicles):
    print("Error: Index out of range")
    exit()

# Access the vehicle at the index and print it
vehicle = vehicles[index]
print("Vehicle at index {}: {}".format(index, vehicle))
