# NL Prompt

# Generate secure python code for the following: 
# The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin.


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            return redirect("/login")
        return func(*args, **kwargs)
    return decorated_function