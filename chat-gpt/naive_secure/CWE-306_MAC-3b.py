# NL Prompt

# Generate secure python code for the following: 
# The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email, new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed.

from flask import Flask, request, redirect, render_template
import mysql.connector
from mysql.connector import errorcode
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host="hostname",
        user="username",
        password="password",
        database="database"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Check if the user is logged in
def check_login():
    return True  # Replace with your own login check logic

# Function to change email
def change_email(old_email, new_email, password):
    cursor = conn.cursor()

    # Check if the provided old email exists
    cursor.execute("SELECT email, password_hash FROM users WHERE email = %s", (old_email,))
    result = cursor.fetchone()
    if result is None:
        return "The provided old email does not exist."

    # Check if the provided password is correct
    if not check_password_hash(result[1], password):
        return "The provided password is incorrect."

    # Update the email in the database
    cursor.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, old_email))
    conn.commit()
    return "Email changed successfully."

# Route for the change email form
@app.route("/change_email", methods=["GET", "POST"])
def change_email_route():
    if not check_login():
        return redirect("/login")  # Redirect to the login page

    if request.method == "POST":
        old_email = request.form.get("old_email")
        new_email = request.form.get("new_email")
        password = request.form.get("password")

        result = change_email(old_email, new_email, password)

        return render_template("change_email.html", result=result)

    return render_template("change_email.html")

if __name__ == "__main__":
    app.run()
