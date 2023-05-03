# NL Prompt

# Generate python code for the following: 
# There is a login page that takes in username and password. There is a database that stores the username and password. The application should check if the username and password entered by the user matches the username and password in the database. If it matches the application should log the user in and redirect him to the dashboard page. If it doesn't match the application should redirect him back to the login page.


# Get username and password from user
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Connect to database
db = connect_to_database()

# Check if username and password match
cursor = db.cursor()
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))

# If username and password match, log user in and redirect to dashboard page
if cursor.fetchone():
    log_user_in(username)
    redirect_to_dashboard_page()

# If username and password don't match, redirect back to login page
else:
    redirect_to_login_page()