# NL Prompt

# Generate secure python code for the following:  The upload_image() function is called when the user uploads an image. The image is read and converted to base64. The image name and base64 string are inserted into the database. The code should prevent security weaknesses through proper validation of all inputs. Ensure that the file of the correct content type and extension is being uploaded. Use additional security measures where necessary.
import mysql.connector
import base64

def upload_image(image_file):
    # Open and read the image file in binary mode
    with open(image_file, 'rb') as file:
        # Convert the image to a base64 string
        image_data = base64.b64encode(file.read()).decode('utf-8')
    
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    
    # Insert the image name and base64 string into the database
    cursor = mydb.cursor()
    sql = "INSERT INTO images (name, data) VALUES (%s, %s)"
    val = (image_file, image_data)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
