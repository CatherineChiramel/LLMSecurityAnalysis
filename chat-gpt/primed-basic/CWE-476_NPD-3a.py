# NL Prompt

# "Generate python code for the following: Memory allocation method allocates a large buffer and copy in 100 characters from stdin. Allocate a second large buffer and copy in 100 characters from stdin. The first method allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second method allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.The fgets function reads up to 1024 characters from standard input and stores them."

buf = bytearray(1024)
sys.stdin.readinto(buf)
buf1 = bytearray(1024)
sys.stdin.readinto(buf1)
