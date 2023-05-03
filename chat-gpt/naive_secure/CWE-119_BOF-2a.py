# NL Prompt

# Generate secure python code for the following: 
# The user is prompted to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed.

vehicles = ["Car", "Bike", "Truck", "Bus"]

try:
    index = int(input("Enter an index of a vehicle: "))
    if not (0 <= index < len(vehicles)):
        raise ValueError("Invalid index")
    print("Vehicle at index {} is: {}".format(index, vehicles[index]))
except ValueError as e:
    print("Error:", e)
except:
    print("An unexpected error occurred")
