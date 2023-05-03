
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Change these to your database credentials and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    is_moderator = db.Column(db.Boolean, default=False)

@app.route('/is_moderator/<username>')
def is_moderator(username):
    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify({'username': user.username, 'is_moderator': user.is_moderator})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
