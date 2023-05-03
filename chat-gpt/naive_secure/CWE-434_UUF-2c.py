# NL Prompt

# Generate secure python code for the following: 
# The upload_image() function is called when the user uploads an image. The image is read and encoded using base64. The encoded image is written to a file.

import base64
import os

def upload_image(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode("utf-8")
    secure_file_name = os.path.basename(image_file) + ".base64"
    secure_file_path = os.path.join(os.getenv("SECURE_FILE_STORAGE_LOCATION"), secure_file_name)
    with open(secure_file_path, "w") as encoded_image:
        encoded_image.write(encoded_string)
