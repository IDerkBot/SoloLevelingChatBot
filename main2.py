from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import calendar
import random
import pymysql

# Connect to database
conn = pymysql.connect(user='root', host='localhost', db='bot', password='1234', autocommit=True)

# auth with group
token = os.environ.get('SOLO_TOKEN')
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def send_message(chat_id, message=None):
    vk_session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})
def del_user(peer_id, user_id):
    vk_session.method('messages.removeChatUser', {'chat_id': peer_id, 'user_id': user_id, 'random_id': random.randint(-2147483648, +2147483648)})

print('Bot Active - \033[32mSuccess\033[0m')

# Получение сообщения и ответ
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                id = str(event.chat_id)  # Номер беседы
                user_id = str(event.user_id)
                response = event.text.lower()  # Сообщение из беседы
                print('msg: ' + response)
                print('user: ' + user_id)
                print('group: ' + id)
                time = str(datetime.strftime(datetime.now(), '%H:%M:%S'))
                data = str(datetime.strftime(datetime.now(), '%Y:%m:%d:%H:%M'))
                print(data)
                data = data.split(':')
                print('time: ' + data[2] + '.' + data[1] + '.' + data[0] + ' ' + data[3] + ':' + data[4])
                print('-' * 30)
                # Для сообщенией из беседы
                if event.from_chat and not event.from_me:
                    if '!kick' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 6:
                            user = str(response[9:18])
                            print(user)
                            del_user(id, user)
    except:
        continue