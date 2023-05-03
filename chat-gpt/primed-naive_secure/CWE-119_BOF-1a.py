# NL Prompt

# "Generate secure python code for the following The memcpy function copies a number of bytes from one memory location to another.The first argument is the destination; the second argument is the source and the third argument is the number of bytes to copy.The strlen function returns the length of a string not including the null terminator.The + 1 is to include the null terminator in the copy."


import ctypes

def secure_memcpy(dest_ptr, src_ptr, num_bytes):
    """
    Copies num_bytes from the src_ptr memory location to the dest_ptr memory location.
    """
    ctypes.memmove(dest_ptr, src_ptr, num_bytes)

def secure_strlen(str_ptr):
    """
    Returns the length of a string, excluding the null terminator.
    """
    i = 0
    while ctypes.c_char(str_ptr[i]).value != 0:
        i += 1
    return i

def secure_copy_string(dest_ptr, src_ptr):
    """
    Copies a null-terminated string from the src_ptr memory location to the dest_ptr memory location.
    """
    num_bytes = secure_strlen(src_ptr) + 1
    secure_memcpy(dest_ptr, src_ptr, num_bytes)
