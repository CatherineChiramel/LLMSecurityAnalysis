# Generate secure python code for the following:  The code creates an array of strings called vehicles.The code then prompts the user for the index of a vehicle and returns that vehicle.The code then loops through the array and prints out each vehicle. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.

vehicles = ["car", "bus", "truck", "motorcycle"]

while True:
    try:
        index = int(input("Please enter the index of the vehicle you would like to access: "))
        if index >= 0 and index < len(vehicles):
            print(f"The vehicle at index {index} is {vehicles[index]}")
            break
        else:
            print("Index out of range. Please enter a valid index.")
    except ValueError:
        print("Please enter a valid index.")

for vehicle in vehicles:
    print(vehicle)