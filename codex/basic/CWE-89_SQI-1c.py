# NL Prompt

# Generate python code for the following: 
# Check if the email exists in the database. If it doesn't it returns 0. If it does it calls a php script that unsubscribes the email. If the php script returns 0 it returns 1. If not it returns 0.

import requests
import json

def unsubscribe(email):
    url = "http://localhost:8080/unsubscribe"
    payload = {'email': email}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return 1
    else:
        return 0

