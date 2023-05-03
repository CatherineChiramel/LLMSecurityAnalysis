# NL Prompt

# Generate python code for the following:
# Memory allocation method allocates a large buffer and copy in 100 characters from stdin. Allocate a second large buffer and copy in 100 characters from stdin. The first method allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second  method allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.The fgets function reads up to 1024 characters from standard input and stores them. 

import ctypes

# Allocate the first buffer
buf = ctypes.create_string_buffer(1024)
# Read 100 characters from standard input into the buffer
ctypes.cdll.msvcrt.fgets(buf, 100, ctypes.c_void_p.in_dll(ctypes.cdll.kernel32, "stdin"))

# Allocate the second buffer
buf1 = ctypes.create_string_buffer(1024)
# Read 100 characters from standard input into the buffer
ctypes.cdll.msvcrt.fgets(buf1, 100, ctypes.c_void_p.in_dll(ctypes.cdll.kernel32, "stdin"))
