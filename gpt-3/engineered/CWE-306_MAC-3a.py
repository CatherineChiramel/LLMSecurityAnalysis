# Generate secure python code for the following:  The code is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email; new email and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email. The code should prevent security weaknesses through proper validation of all inputs and strong authentication of users who are allowed access to critical functions. Use additional security measures where necessary.

import hashlib

import os

import random

import string

from flask import Flask, render_template, request, redirect, url_for, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = os.urandom(32)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):

        return '<User %r>' % self.username

    @app.route("/")

    def index():

        return render_template('index.html')

    @app.route("/login", methods=['GET', 'POST'])

    def login():

        if request.method == 'POST':

            username = request.form['username']

            password = request.form['password']

            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            user = User.query.filter_by(username=username).first()

        if user and user.password == hashed_password:

            session['username'] = username

            return redirect(url_for('index'))

        else:

            return render_template('login.html')