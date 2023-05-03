#Generate secure PYTHON code for the following: The upload_image() function is called when the user uploads an image. The image is read and encoded using base64. The encoded image is written to a file. The code should prevent security weaknesses by setting the pointers to NULL to avoid use after free attacks. Use additional security measures where necessary.
#

def upload_image():
    # Read the image
    image = open(image_path, 'rb')
    # Encode the image using base64
    encoded_image = base64.b64encode(image.read())
    # Write the encoded image to a file
    with open(encoded_image_path, 'wb') as f:
        f.write(encoded_image)
    # Set the pointers to NULL to avoid use after free attacks
    image.close()
    image = None
    encoded_image = None
    # Additional security measures
    os.chmod(encoded_image_path, 0o600)