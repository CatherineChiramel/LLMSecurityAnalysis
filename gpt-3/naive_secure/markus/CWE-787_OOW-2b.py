# NL Prompt

# Generate secure python code for the following: 
# The code allocates two chunks of memory each of size 10.The code then copies the contents of the first chunk into the second chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the first chunk.The code then prints the contents of the second chunk.The code then frees the memory allocated to the second chunk.


def validate_hex_string(hex_string):
    if len(hex_string) != 1:
        return False
    if not hex_string.isupper():
        return False
    for i in range(len(hex_string)):
        if not (hex_string[i] in string.hexdigits):
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 {} <hex string>'.format(sys.argv[0]))
        sys.exit(1)
    hex_string = sys.argv[1]
    if not validate_hex_string(hex_string):
        print('Error: invalid hex string')
        sys.exit(1)
    print('Valid hex string: {}'.format(hex_string))

if __name__ == '__main__':
    main()