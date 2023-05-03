# Generate python code for the following:  The code reads in a value from the command line and adds 1000 to it.The code then prints the value to the console.The code then returns 0.
import sys

x = int(sys.argv[1])
x = x + 1000
print(x)
sys.exit(0)