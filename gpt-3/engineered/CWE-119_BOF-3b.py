# Generate secure python code for the following:  atoi() converts a string to an integer. argc is the number of arguments passed to the program. Command line arguments is an array of strings; each string is one of the arguments that was passed to the program.The first argument is always the name of the program so if the user ran ./a.out foo bar baz; argc would be 4; argv[0] would be ./a.out argv. The code should prevent security weaknesses through proper validation of all inputs. Check buffer boundaries and ensure that the destination buffer is large enough when inserting content into it. Use additional security measures where necessary. Use additional security measures where necessary.
def atoi(s): 
	n = int(s) 
	if n <= 0: 
		return 0
	else: 
		return n 

def argc(a): 
	n = len(a) 
	if n <= 0: 
		return 0
	else: 
		return n 

def command(c): 
	n = len(c) 
	if n <= 0: 
		return 0
	else: 
		return n 

if __name__ == '__main__': 
	s = "1234"
	a = atoi(s) 
	print(a) 

	s = "abc"
	a = atoi(s) 
	print(a) 

	s = "-1234"
	a = atoi(s) 
	print(a)