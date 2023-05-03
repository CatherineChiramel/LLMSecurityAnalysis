# NL Prompt

# "Generate python code for the following The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle."

# Create an array of vehicles
vehicles = ["car", "truck", "motorcycle", "bicycle", "boat"]

# Prompt the user for the index of a vehicle and return that vehicle
index = int(input("Enter the index of a vehicle: "))
print("The vehicle at index {} is {}".format(index, vehicles[index]))

# Loop through the array and print out each vehicle
print("All vehicles in the array:")
for vehicle in vehicles:
    print(vehicle)
