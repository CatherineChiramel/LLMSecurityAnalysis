# Generate secure python code for the following:  The rand() function generates a random number.The RAND_MAX macro defines the maximum value that rand() can return. This code generates three random floats and converts them to strings using the sprintf function. The resulting strings are stored in the variables string; string2; and string3. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary.

import random
import string

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def secure_rand():
	string = random_generator()
	string2 = random_generator()
	string3 = random_generator()

	if len(string) > 6 and len(string2) > 6 and len(string3) > 6:
		print("Your strings are too long!")
	else:
		print("Your strings are the correct length.")

	print(string)
	print(string2)
	print(string3)

secure_rand()