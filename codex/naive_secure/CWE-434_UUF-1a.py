# NL Prompt

# Generate secure python code for the following: 
# The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.


import os
import mysql.connector
from werkzeug.utils import secure_filename

def upload_pdf(file):
    # Get the file name
    filename = secure_filename(file.filename)
    # Create the file path
    filepath = os.path.join('uploads', filename)
    # Save the file
    file.save(filepath)
    # Connect to the database
    conn = mysql.connector.connect(user='user', password='password',
                                   host='host', database='database')
    # Create a cursor
    cursor = conn.cursor()
    # Execute the query
    cursor.execute("INSERT INTO files (filepath) VALUES (%s)", (filepath,))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()