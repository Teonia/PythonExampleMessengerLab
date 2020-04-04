import requests
from datetime import datetime
import time

endpoint_uri_send = 'http://127.0.0.1:5000/send'
endpoint_uri_messages = 'http://127.0.0.1:5000/messages'
after = 0


def view_messages():
    response = requests.get(endpoint_uri_messages, params={'after': after})
    if response.text is not None:
        if response.text != '':
            data = response.json()
            return data['messages']


while True:
    messages = view_messages()
    for message in messages:
        text = message['text']
        timestamp = datetime.fromtimestamp(message['time']).isoformat()
        if text != '':
            print(f"[{timestamp}] {message['username']}: {message['text']}")
        if message['time'] > after:
            after = message['time']

    time.sleep(1)
