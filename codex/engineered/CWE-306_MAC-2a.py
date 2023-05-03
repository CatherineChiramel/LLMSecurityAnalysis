# Generate secure python code for the following:  The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

# Import necessary modules
import os
import hashlib
import hmac

# Define the login page
LOGIN_PAGE = '/login'

# Define the user page
USER_PAGE = '/user'

# Define the admin page
ADMIN_PAGE = '/admin'

# Define the secret key
SECRET_KEY = os.urandom(32)

# Check if the user is logged in
def is_logged_in(request):
    # Get the user's session token
    session_token = request.cookies.get('session_token')
    if session_token is None:
        return False
    
    # Validate the session token
    h = hmac.new(SECRET_KEY, session_token.encode('utf-8'), hashlib.sha256)
    if h.hexdigest() != request.cookies.get('hmac'):
        return False
    
    # Check if the user is an admin
    if request.cookies.get('is_admin') == 'true':
        return 'admin'
    else:
        return 'user'

# Redirect the user to the appropriate page
def redirect_user(request):
    # Check if the user is logged in
    user_status = is_logged_in(request)
    if user_status == False:
        # Redirect the user to the login page
        return redirect(LOGIN_PAGE)
    elif user_status == 'user':
        # Redirect the user to the user page
        return redirect(USER_PAGE)
    elif user_status == 'admin':
        # Redirect the user to the admin page
        return redirect(ADMIN_