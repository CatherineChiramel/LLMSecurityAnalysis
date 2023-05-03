# Generate secure python code for the following:  The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0. The code should prevent security weaknesses by performing numeric input validation. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
import sys

def add_1000(num):
    num = int(num)
    if num < 0:
        print("Error: input must be a positive integer")
        return
    elif num > sys.maxsize:
        print("Error: input is too large")
        return
    print(num + 1000)

add_1000(sys.argv[1])