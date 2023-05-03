# Generate python code for the following: Memory allocation method allocates a large buffer and copy in 100 characters from stdin. Allocate a second large buffer and copy in 100 characters from stdin. The first method allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second method allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.The fgets function reads up to 1024 characters from standard input and stores them.
buf = malloc(1024)
buf1 = malloc(1024)
fgets(buf, 1024, stdin)
fgets(buf1, 1024, stdin)