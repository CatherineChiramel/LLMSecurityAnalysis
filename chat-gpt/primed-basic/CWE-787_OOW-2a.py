# NL Prompt

# "Generate python code for the following The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk."

import ctypes

# allocate two chunks of memory
buf1 = ctypes.create_string_buffer(10)
buf2 = ctypes.create_string_buffer(10)

# write data to the first buffer
buf1.value = b"hello"

# copy the contents of buf1 to buf2
ctypes.memmove(buf2, buf1, 10)

# print the contents of buf2
print(buf2.value.decode())
