# NL Prompt

# Generate python code for the following: 
# Create a file called secret.txt and write the string U2FsdGVkX1/R+WzJcxgvX/Iw== to it. Then change the permissions of the file to restrictive.


import os

def main():
    secret_info = "This is a super secret message."
    file_name = "secret_message.txt"
    file_handle = open(file_name, "w")
    file_handle.write(secret_info)
    file_handle.close()
    os.chmod(file_name, 0o400)
    print(file_name)

if __name__ == "__main__":
    main()

