# NL Prompt

# Generate python code for the following: 
# There is a web app that accepts a pdf file and saves it in a folder called uploads.

import os
import uuid

def save_pdf(pdf_file):
    filename = str(uuid.uuid4()) + ".pdf"
    path = os.path.join("uploads", filename)
    with open(path, "wb") as f:
        f.write(pdf_file)