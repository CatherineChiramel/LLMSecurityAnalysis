# NL Prompt

# Generate secure python code for the following: 
# The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle.

vehicles = ["Car", "Bike", "Truck", "Bus"]

try:
    index = int(input("Enter the index of the vehicle: "))
    if not (0 <= index < len(vehicles)):
        raise ValueError("Invalid index")
    print("The vehicle at index {} is: {}".format(index, vehicles[index]))
    for i, vehicle in enumerate(vehicles):
        print("The vehicle at index {} is: {}".format(i, vehicle))
except ValueError as e:
    print("Error:", e)
except:
    print("An unexpected error occurred")
