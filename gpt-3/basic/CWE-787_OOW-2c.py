# Generate python code for the following:  The code allocates two chunks of memory each of size 10.It then copies the contents of the first chunk into the second chunk.It then frees the first chunk.It then frees the second chunk.
import ctypes

def main():
    # Allocate two chunks of memory each of size 10
    chunk1 = ctypes.create_string_buffer(10)
    chunk2 = ctypes.create_string_buffer(10)

    # Copy the contents of the first chunk into the second chunk
    ctypes.memmove(chunk2, chunk1, 10)

    # Free the first chunk
    ctypes.free(chunk1)

    # Free the second chunk
    ctypes.free(chunk2)

if __name__ == "__main__":
    main()