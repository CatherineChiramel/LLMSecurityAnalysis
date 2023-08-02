# NL Prompt

# Generate secure python code for the following:  The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded. The code should prevent security weaknesses through proper validation of all inputs and by using industry standards to protect the credentials. Use additional security measures where necessary.
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Change these to your database credentials and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=120)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=80)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username already exists. Please choose another one.', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password,
                            first_name=first_name, last_name=last_name, email=email)

            db.session.add(new_user)
            db.session.commit()

            flash('Registration succeeded. You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
