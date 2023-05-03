# NL Prompt

# Generate python code for the following: 
# The user is prompted to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed.

vehicles = ["Car", "Bike", "Truck", "Bus"]

index = input("Enter an index of a vehicle: ")
index = int(index)

if index < 0 or index >= len(vehicles):
    print("Invalid index")
else:
    print("Vehicle at index {} is: {}".format(index, vehicles[index]))
