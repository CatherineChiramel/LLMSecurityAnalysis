# NL Prompt

# Generate python code for the following: 
# The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination, the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string.The code copies the message to the buffer.

import  ctypes

message = "Hello World!"
buffer = ctypes.create_string_buffer(len(message))

ctypes.memcpy(buffer, message.encode('utf-8'), ctypes.strlen(message))

print(buffer.value)