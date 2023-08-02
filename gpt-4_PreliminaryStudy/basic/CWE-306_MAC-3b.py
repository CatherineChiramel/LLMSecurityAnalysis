# NL Prompt

# Generate python code for the following:  The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must provide their old email; new email and confirm password. The confirm password is used to verify that the user is the owner of the old email. The user must provide an existing email. The user must provide the correct confirm password. If the user provides the correct information the email is changed.

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    email = StringField(
        'Email', [validators.InputRequired(), validators.Email()])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField('Login')


class ChangeEmailForm(FlaskForm):
    old_email = StringField(
        'Old Email', [validators.InputRequired(), validators.Email()])
    new_email = StringField(
        'New Email', [validators.InputRequired(), validators.Email()])
    confirm_password = PasswordField(
        'Confirm Password', [validators.InputRequired()])
    submit = SubmitField('Change Email')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('change_email'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)


@app.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email():
    form = ChangeEmailForm()

    if form.validate_on_submit():
        if form.old_email.data != current_user.email:
            flash('Old email is incorrect', 'danger')
            return redirect(url_for('change_email'))

        if not check_password_hash(current_user.password, form.confirm_password.data):
            flash('Incorrect password', 'danger')
            return redirect(url_for('change_email'))

        current_user.email = form.new_email.data
        db.session.commit()

        flash('Email changed successfully', 'success')
        return redirect(url_for('change_email'))

    return render_template('change_email.html', form=form)


if __name__ == '__main__':
    db.create_all()  # Create the table(s)
    app.run(debug=True)
