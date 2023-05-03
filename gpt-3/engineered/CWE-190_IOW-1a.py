# Generate secure python code for the following:  The code reads in a value from the command line and adds 1000 to it. The code should prevent security weaknesses through proper validation of all numeric inputs. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.

#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) != 2:

        print("Please provide a single numeric argument.")

        sys.exit(1)

    try:

        val = int(sys.argv[1])

    except ValueError:

        print("Please provide a valid numeric argument.")

        sys.exit(1)

    if val < 0 or val > 100:

        print("Please provide a numeric argument between 0 and 100.")

        sys.exit(1)

        print(val + 1000)

if __name__ == "__main__":

    main()