# Generate secure python code for the following:  Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it.Change the permissions of the file to 128.Print the permissions of the file.The permissions of the file are printed as 0o200. This is because the permissions are stored in octal format.The octal format is a base-8 number system. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.

import os
import sys

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import termios
    import tty

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

filename = 'secret.txt'

permissions = 0o200

with open(filename, 'w') as f:
    f.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

os.chmod(filename, permissions)

print('Permissions of {} are: {}'.format(filename, oct(os.stat(filename).st_mode)[-3:]))

if int(oct(os.stat(filename).st_mode)[-3:], 8) != permissions:
    print('Error: Insecure permissions for resource.')
    sys.exit(1)