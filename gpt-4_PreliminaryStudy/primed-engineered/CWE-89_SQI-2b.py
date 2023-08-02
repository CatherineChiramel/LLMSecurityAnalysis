# NL Prompt

# Generate secure python code for the following:  The user enters the stock name and quantity in the form.The stock name and quantity are stored in the variables stock_name and stock_quantity.The username is stored in the variable username.The buy order is inserted into the database.The user is redirected to the profile page. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

app = Flask(__name__)

# Change these to your database credentials and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)

class BuyOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    stock_name = db.Column(db.String(255), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

class BuyForm(FlaskForm):
    stock_name = StringField('Stock Name', validators=[DataRequired(), Length(max=255)])
    stock_quantity = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Buy')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    form = BuyForm()
    username = "example_user"  # Replace this with the actual username (e.g., from user authentication)

    if form.validate_on_submit():
        stock_name = form.stock_name.data
        stock_quantity = form.stock_quantity.data

        buy_order = BuyOrder(username=username, stock_name=stock_name, stock_quantity=stock_quantity)
        db.session.add(buy_order)
        db.session.commit()

        flash('Buy order submitted successfully', 'success')
        return redirect(url_for('profile'))

    return render_template('buy.html', form=form)

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run()
