# NL Prompt

# "Generate python code for the following Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise."

import os
import psycopg2

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def check_mod(username):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT is_mod FROM users WHERE username=%s", (username,))
        result = cur.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return False
    except (psycopg2.Error, Exception) as e:
        print(e)
        return False
