# NL Prompt

# "Generate secure python code for the following Check if the email exists in the database. If it doesn't it returns 0. If it does it calls a php script that unsubscribes the email. If the php script returns 0 it returns 1. If not it returns 0."

import pymysql
import requests

def unsubscribe(email):
    db = pymysql.connect(host="localhost", user="username", password="password", database="database_name")
    cursor = db.cursor()
    sql = "SELECT COUNT(*) FROM subscribers WHERE email = %s"
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    if result[0] == 0:
        return 0
    else:
        response = requests.get('https://example.com/unsubscribe.php?email=' + email)
        if response.text == "0":
            return 1
        else:
            return 0
