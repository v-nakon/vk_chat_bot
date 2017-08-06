from flask import Flask, request, json
import messageHandler
from multiprocessing import Queue

app = Flask(__name__)

# токен моего приложения
secret_token = ''

# токены моего сообщества
token = ''
confirmation_token = ''

queue = Queue()


@app.route('/')
def hello_world():
    return 'chat_bot'

#запуск потоков
@app.before_first_request
def start():
    messageHandler.run_threads()

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