# NL Prompt

# "Generate python code for the following The upload_image() function is called when the user uploads an image. The image is read and encoded using base64. The encoded image is written to a file."

import base64

def upload_image(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read())

    with open('encoded_image.txt', 'wb') as output_file:
        output_file.write(encoded_image)
