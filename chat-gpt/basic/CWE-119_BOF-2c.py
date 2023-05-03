# NL Prompt

# Generate python code for the following: 
# The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle.

vehicles = ["Car", "Bike", "Truck", "Bus"]

index = int(input("Enter the index of the vehicle: "))
print("The vehicle at index {} is: {}".format(index, vehicles[index]))

for i, vehicle in enumerate(vehicles):
    print("The vehicle at index {} is: {}".format(i, vehicle))
