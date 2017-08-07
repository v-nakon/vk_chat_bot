
from flask import Flask, request, json
import messageHandler
from multiprocessing import Queue

app = Flask(__name__)
messageHandler.run_threads()


# токены моего сообщества
confirmation_token = 'ea065d90'

queue = Queue()


@app.route('/')
def hello_world():
    return 'chat_bot'


@app.route('/', methods=['POST'])
def processing():
    global queue

    print("start processing")
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        print("start message")
        queue.put(data)

        #messageHandler.create_answer(data['object'], token, secret_token)
        return 'ok'
