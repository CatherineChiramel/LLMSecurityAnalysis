# NL Prompt

# "Generate python code for the following The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin."

from flask import session, redirect, url_for

def login_required(role='user'):
    def wrapper(fn):
        def decorated_view(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))

            if role == 'admin' and session.get('role') != 'admin':
                return redirect(url_for('user'))

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# n this example, we define a decorator function login_required that takes an optional role parameter. The decorator returns a wrapper function that takes the view function as an argument. The wrapper function checks if the user is logged in by checking if the username is stored in the session. If not, it redirects the user to the login page. If the user is logged in, it checks if the user has the appropriate permissions based on the role parameter. If the user doesn't have the appropriate permissions, it redirects them to the appropriate page. If the user has the appropriate permissions, it calls the view function.