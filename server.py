import datetime
import time
from flask import Flask, request, abort


app = Flask("messenger")
messages = [
    {'username': 'Nick', 'text': 'Hello', 'time': 0.0}
]
registered_users = {}


@app.route("/")
def hello():
    return "Hello, world>"


#
#
@app.route("/status")
def status():
    """
    :return: JSON {
        "status": Boolean, "name": str, "users_count": number, "messages_count": number, "time": str
    }
    """
    return {
        'status': True,
        'name': app.name,
        'users_count': len(registered_users),
        'messages_count': len(messages),
        'time': datetime.datetime.now().isoformat()
        # 'time': datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    }


@app.route("/send", methods=['POST'])
def send():
    """
    receives JSON
    {
        "username": str,
        "password": str,
        "text": str
    }
    :return: JSON {"ok": true}
    """
    username = request.json['username']
    password = request.json['password']

    if username in registered_users:
        if password != registered_users[username]:
            return abort(401)
    else:
        registered_users[username] = password

    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)
    print(request.json)
    return {"ok": True}


@app.route("/messages", methods=['GET'])
def messages_view():
    """
    receives ?after=float
    :return: JSON {
    "messages": [
        {"username" str, "text": str, "time: float}
        ...
        ]
    }
    """
    after = float(request.args.get('after'))
    # filtered_messages = []
    # for message in messages:
    #     if message['time'] > after:
    #         filtered_messages.append(message)
    filtered_messages = [message for message in messages if message['time'] > after]
    timestamp = datetime.datetime.now().isoformat()
    print(timestamp + "____")
    messages_ = {
        'timestamp': timestamp,
        'messages': filtered_messages
    }
    print(messages_)
    print(timestamp + "____")
    return messages_


app.run()
