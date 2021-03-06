import vkapi
import numpy as n
import flask_app as fl
import threading
import time

#список для токенов
list_seckret_tokens = [""]
token = ""

list1 = ["держи", "лови", "бери", "забирай", "принимай", "зацени"]
list2 = ["крутой", "классный", "отпадный", "прикольный", "смешной", "веселый"]
list3 = ["крутую", "классную", "отпадную", "прикольную", "смешную", "веселую"]
list4 = ["не то вводишь", "смотри ниже что нужно вводить", "введи слова которые предлагают ниже"]


#проверка очереди, ответ на запрос
def get_queue(secret_token):
    while True:
        if fl.queue.empty() == False:
            data = fl.queue.get_nowait()
            print("Get DATA")
            create_answer(data['object'], token, secret_token)
        else:
            print("Queue is empty")
            time.sleep(2)




#запуск потоков
def run_threads():
    for s_token in list_seckret_tokens:
        thread_ = threading.Thread(target = get_queue, args = (s_token))
        thread_.start()
        print("run thread")



# рандомное слово
def rnd_word(list):
    rnd_word = n.random.choice(list, 1)
    return ''.join(rnd_word)


# ответ на сообщение пользователя
def get_answer(body, secret_token, user_id):
    name = vkapi.user_get(user_id, secret_token)
    link = ''
    if body == 'haha':
        message = '%s, %s %s анекдот! \n %s\n\n' % (name, rnd_word(list1), rnd_word(list2), vkapi.wall_get_joke(secret_token))
    elif body == 'haha_gif':
        message, link = vkapi.wall_get_video(secret_token)
        message = '%s, %s %s гифку! \n %s \n\n' % (name, rnd_word(list1), rnd_word(list3), message)
    else:
        message = '%s, %s\n\n' % (name, rnd_word(list4))
    return message, link


# ответ пользователю
def create_answer(data, token, secret_token):
    text = '\nНапиши: \nhaha - получишь анекдот \nhaha_gif - получишь гифку'

    user_id = data['user_id']
    message, link = get_answer(data['body'].lower(), secret_token, user_id)
    vkapi.send_message(user_id, token, message, link)
    vkapi.send_message(user_id, token, text, '')
