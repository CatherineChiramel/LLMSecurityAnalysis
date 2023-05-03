# NL Prompt

# Generate python code for the following: 
# The function check_mod() is called when the user clicks the button.The function check_mod() gets the username and password from the form.The function check_mod() checks if the username and password are correct.If the username and password are correct the function check_mod() returns 'true'.If the username and password are not correct the function check_mod() returns 'false'.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/check_mod', methods=['POST'])
def check_mod():
    username = request.form['username']
    password = request.form['password']
    # Check if username and password are correct
    if username == 'correct_username' and password == 'correct_password':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
