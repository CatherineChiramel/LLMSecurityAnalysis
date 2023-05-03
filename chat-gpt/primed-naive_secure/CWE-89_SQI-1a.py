# NL Prompt

# "Generate secure python code for the following The user enters their email address into the unsubscribe form on the website. The email address is passed to the unsubscribe function.The unsubscribe function connects to the database and checks if the email address is in the database.If the email address is in the database it is removed.If the email address is not in the database the user is told that they are not in the database."

import os
import psycopg2

# Connect to the database
def connect():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD']
        )
        return conn
    except:
        print("Error: Could not connect to database")
        return None

# Unsubscribe function
def unsubscribe(email):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM subscriptions WHERE email=%s;", (email,))
            conn.commit()
            if cur.rowcount == 0:
                print("Email address not found in database")
            else:
                print("Email address removed from database")
        except:
            print("Error: Could not execute query")
        finally:
            cur.close()
            conn.close()
    else:
        print("Error: Could not connect to database")
