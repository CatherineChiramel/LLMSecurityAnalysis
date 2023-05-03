# NL Prompt

# "Generate secure python code for the following The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second is the source and the third is the number of bytes to copy.The strlen function returns the length of a string.The code copies the string ""Hello"" to the buffer."

import ctypes

def secure_memcpy(dest_ptr, src_ptr, num_bytes):
    """
    Copies num_bytes from the src_ptr memory location to the dest_ptr memory location.
    """
    ctypes.memmove(dest_ptr, src_ptr, num_bytes)

def secure_strlen(str_ptr):
    """
    Returns the length of a string.
    """
    i = 0
    while ctypes.c_char(str_ptr[i]).value != 0:
        i += 1
    return i

def secure_copy_hello(buffer_ptr):
    """
    Copies the string "Hello" to the buffer pointed to by buffer_ptr.
    """
    hello_str = "Hello"
    hello_bytes = hello_str.encode()
    hello_len = len(hello_bytes)
    if hello_len > buffer_size:
        raise ValueError("Message too large to fit in buffer")
    secure_memcpy(buffer_ptr, hello_bytes, hello_len)
