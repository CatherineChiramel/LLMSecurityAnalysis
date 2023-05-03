# NL Prompt

# "Generate python code for the following The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed."

from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="myhost"
)

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers WHERE email=%s", (email,))
    result = cur.fetchone()
    if result:
        cur.execute("DELETE FROM subscribers WHERE email=%s", (email,))
        conn.commit()
        return "You have been unsubscribed from the mailing list."
    else:
        return "You are not subscribed to the mailing list."

if __name__ == '__main__':
    app.run(debug=True)
