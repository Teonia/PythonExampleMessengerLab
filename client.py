import requests
import time

endpoint_uri_send = 'http://127.0.0.1:5000/send'
#
# response = requests.get('http://127.0.0.1:5000/status')
# print(response.status_code)
# print(response.text)
# print(response.json())
#
# message = {'username': 'user', 'text': '123'}
# response = requests.post(endpoint_uri_send, json=message)
# print(response.status_code)
# print(response.text)
# print(response.json())


def send_message(username, password, text):
    message = {'username': username, 'password': password, 'text': text}
    response = requests.post(endpoint_uri_send, json=message)
    if response.status_code != 200:
        print("Error")


username = input('Enter name> ')
password = input('Password> ')

while True:
    text = input()
    if text == 'exit':
        break
    send_message(username, password, text)

