# NL Prompt

# Generate python code for the following:  The user is redirected to the login page if he/she is not logged in. The user is redirected to the user page if he/she is logged in. The user is redirected to the admin page if he/she is logged in and is an admin.

from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager, login_user, login_required, current_user, UserMixin

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # This should be a secret!

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Sample user database (for illustration purposes only). Use a real database in production.
users = {
    'user1': {'password': 'password1', 'is_admin': False},
    'admin1': {'password': 'password_admin', 'is_admin': True}
}


class User(UserMixin):
    def __init__(self, id, is_admin=False):
        self.id = id
        self.is_admin = is_admin


@login_manager.user_loader
def load_user(user_id):
    user_data = users.get(user_id)
    if user_data:
        return User(id=user_id, is_admin=user_data['is_admin'])
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if users.get(username) and users[username]['password'] == password:
            user = User(id=username, is_admin=users[username]['is_admin'])
            login_user(user)
            return redirect(url_for('user_page'))
    return render_template('login.html')


@app.route('/user')
@login_required
def user_page():
    if current_user.is_admin:
        return redirect(url_for('admin_page'))
    return render_template('user.html')


@app.route('/admin')
@login_required
def admin_page():
    if not current_user.is_admin:
        return redirect(url_for('user_page'))
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
