import vk
import random

session = vk.Session()
api = vk.API(session, v=5.67)

# отправка сообщения
def send_message(user_id, token, message, attachment=""):
	check = 0
	while check <= 4:
		try:
			api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)
			break
		except:
			check += 1
	print("error send message")
	

# получение текста с группы
def wall_get_joke(secret_token):
	check = 0
	while check <= 4:
		try:
			response = api.wall.get(access_token = secret_token, owner_id= str(-29385594), count=str(100))
			rnd = random.randint(0,99)
			return response['items'][rnd]['text']
		except:
			check += 1
	print("error wall_get_joke")


# получение текста и ссылки с группы
def wall_get_video(secret_token):
	check = 0
	while check <= 4:
		try:
			response = api.wall.get(access_token=secret_token, owner_id=str(-6877026), count=str(100))
			rnd = random.randint(0, 99)
			text = response['items'][rnd]['text']
			id = response['items'][rnd]['attachments'][0]['doc']['id']
			owner_id = response['items'][rnd]['attachments'][0]['doc']['owner_id']
			link = 'doc' + str(owner_id) + '_' + str(id)
			return text, link
		except:
			check += 1
	print("error wall_get_video")


# получение имени пользователя
def user_get(user_id, secret_token):
	check = 0
	while check <= 4:
		try:
			response = api.users.get(access_token = secret_token, user_ids = str(user_id))
			first_name = response[0]['first_name']
			return first_name
		except:
			check += 1
	print("error user_get")
	
