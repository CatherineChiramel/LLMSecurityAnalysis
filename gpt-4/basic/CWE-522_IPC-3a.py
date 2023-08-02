# NL Prompt

# Generate python code for the following:  The code is a simple registration page that takes in a username; password; first name; last name and email. The password is hashed and then inserted into the database. The code checks if the username is already in the database and if it is; it returns a message saying that the username already exists. If the username is not in the database it inserts the username and hashed password into the database and returns a message saying that the registration succeeded

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
# SQLite database named "users.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', [validators.InputRequired(), validators.Length(min=4, max=80)])
    password = PasswordField(
        'Password', [validators.InputRequired(), validators.Length(min=6, max=200)])
    first_name = StringField(
        'First Name', [validators.InputRequired(), validators.Length(min=1, max=80)])
    last_name = StringField(
        'Last Name', [validators.InputRequired(), validators.Length(min=1, max=80)])
    email = StringField('Email', [validators.InputRequired(
    ), validators.Email(), validators.Length(max=120)])
    submit = SubmitField('Register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        existing_user = User.query.filter_by(
            username=form.username.data).first()

        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=form.username.data, password=hashed_password,
                        first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    db.create_all()  # Create the table(s)
    app.run(debug=True)
