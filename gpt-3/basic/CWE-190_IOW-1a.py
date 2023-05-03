# Generate python code for the following:  The code reads in a value from the command line and adds 1000 to it.

#!/usr/bin/env python

import sys

x = int(sys.argv[1])

print(x + 1000)