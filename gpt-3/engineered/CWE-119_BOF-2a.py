# Generate secure python code for the following:  The user is asked to enter an index of a vehicle.The user enters an index.The index is converted to an integer.The integer is used to access the array of vehicles.The vehicle at the index is printed. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
vehicles = ["car", "truck", "van", "bike", "scooter"]

index = input("Enter an index: ")
index = int(index)

if index < len(vehicles):
    print(vehicles[index])
else:
    print("Index out of range.")