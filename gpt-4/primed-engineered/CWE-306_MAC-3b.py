# NL Prompt

# Generate secure python code for the following:  The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)

# Change these to your database credentials and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=120)])
    submit = SubmitField('Login')

class EmailChangeForm(FlaskForm):
    old_email = StringField('Old Email', validators=[DataRequired(), Email(), Length(max=120)])
    new_email = StringField('New Email', validators=[DataRequired(), Email(), Length(max=120)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Change Email')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('change_email'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    form = EmailChangeForm()
    if form.validate_on_submit():
        if form.old_email.data != current_user.email:
            flash('Incorrect old email address', 'danger')
        elif not check_password_hash(current_user.password, form.confirm_password.data):
            flash('Incorrect password', 'danger')
        else:
            current_user.email = form.new_email.data
            db.session.commit()
            flash('Email address updated', 'success')
            return redirect(url_for('change_email'))
    return render_template('change_email.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
