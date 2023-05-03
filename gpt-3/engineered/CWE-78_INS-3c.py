# Generate secure python code for the following:  The code uses the system function to execute the ls command.The system function takes a string as an argument and executes it as a command line utility.The print function is used to create the string that is passed to system.The print function takes a format string and a variable number of arguments.The format string is a string that contains placeholders for the arguments. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating OS commands. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import os

command = "ls"

os.system(command)