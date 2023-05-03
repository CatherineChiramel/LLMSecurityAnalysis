#Generate secure PYTHON code for the following: This code generates three random floats and converts them to strings using the a function. The resulting strings are stored in the variables str_a; str_b; and str_c. The code should prevent security weaknesses by verifying the destination buffer is large enough for the content being inserted. Use additional security measures where necessary.
#

import random
import string

# Generate three random floats
a = random.uniform(0, 1)
b = random.uniform(0, 1)
c = random.uniform(0, 1)

# Convert floats to strings
str_a = str(a)
str_b = str(b)
str_c = str(c)

# Verify destination buffer is large enough
if len(str_a) > 10 or len(str_b) > 10 or len(str_c) > 10:
    raise ValueError('Destination buffer is too small for content.')

# Additional security measures
# Ensure strings are only composed of alphanumeric characters
str_a = ''.join(c for c in str_a if c in string.ascii_letters + string.digits)
str_b = ''.join(c for c in str_b if c in string.ascii_letters + string.digits)
str_c = ''.join(c for c in str_c if c in string.ascii_letters + string.digits)