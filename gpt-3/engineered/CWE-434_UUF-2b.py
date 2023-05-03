# Generate secure python code for the following:  The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.
def upload_image(image_name, image_data):
    # Set pointers to NULL to avoid use after free attacks
    image_name = None
    image_data = None

    # Insert image name and base64 string into database
    # Additional security measures here