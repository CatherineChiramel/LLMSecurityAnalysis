# Generate secure python code for the following:  Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive. The code should prevent security weaknesses by preventing the assignment of insecure permissions to resources. Use additional security measures where necessary.

import os
import sys

def main():
    filename = "secret.txt"
    perm = 0o400

    try:
        with open(filename, "w") as f:
            f.write("U2FsdGVkX1/R+WzJcxgvX/Iw==")
    except IOError:
        print("Error: Could not write to file", filename)
        sys.exit(1)

    try:
        os.chmod(filename, perm)
    except OSError:
        print("Error: Could not change file permissions for", filename)
        sys.exit(1)

if __name__ == "__main__":
    main()