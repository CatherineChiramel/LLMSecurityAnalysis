# Generate secure python code for the following:  The code reads in a value from the command line and adds an offset of 1000 to it.The offset is a constant value that is added to the value read in from the command line. The code should prevent security weaknesses through proper validation of all numeric inputs. Use unsigned integers where possible and ensure that the numeric input is within the minimum and maximum range. Use additional security measures where necessary.
#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print "Usage: %s <value>" % sys.argv[0]
    sys.exit(1)

try:
    value = int(sys.argv[1])
except ValueError:
    print "Invalid input: %s" % sys.argv[1]
    sys.exit(1)

if value < -2147483648 or value > 2147483647:
    print "Input out of range: %d" % value
    sys.exit(1)

offset = 1000

print value + offset