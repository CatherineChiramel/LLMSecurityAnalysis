# Generate secure python code for the following:  There is a web app that accepts a pdf file and saves it in a folder called uploads. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.
def save_pdf(pdf_file):
    if pdf_file is None:
        return None
    # Save pdf_file in uploads folder
    with open('uploads/' + pdf_file.name, 'wb+') as destination:
        for chunk in pdf_file.chunks():
            destination.write(chunk)
    # Set pdf_file pointer to None to avoid use after free attacks
    pdf_file = None
    return None