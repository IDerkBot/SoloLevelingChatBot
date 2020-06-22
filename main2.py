from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import pymysql

# Connect to database
conn = pymysql.connect(user='root', host='localhost', db='bot', password='1234', autocommit=True)

# auth with group
token = 'e1cbc53af2fb1f1e0376570db03e6e5e2414c698ea31388d9f5872e0153d1a1d5295994fbb7f4e06c99d6'
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def send_message(chat_id, message=None):
    vk_session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})
def del_user(chat_id, user_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM `users` WHERE (`uid` = '" + user_id + "')")
    vk_session.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': user_id, 'random_id': random.randint(-2147483648, +2147483648)})
print('Bot Active - \033[32mSuccess\033[0m')


# Получение сообщения и ответ
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                id = str(event.chat_id)  # Номер беседы
                user_id = str(event.user_id)
                response = event.text.lower()  # Сообщение из беседы
                user = vk_session.method("users.get", {"user_ids": user_id})
                fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                print('msg: ' + response)
                print('name: ' + fullname)
                print('user: ' + user_id)
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                    rows = cursor.fetchall()
                    complain = rows[0][14]
                    if complain >= 3:
                        del_user(id, user_id)
                    else:
                        if event.from_chat and not event.from_me:
                            if '!подставить' in response:
                                with conn.cursor() as cursor:
                                    cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                                    rows = cursor.fetchall()
                                    rang_request = str(rows[0][3])
                                    user_request = str(rows[0][1])
                                    if int(rows[0][3]) >= 6:
                                        user = str(response[15:24])
                                        cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user + "'")
                                        rows = cursor.fetchall()
                                        rang_kick = str(rows[0][3])
                                        print(rang_request)
                                        print(rang_kick)
                                        if rang_request > rang_kick:
                                            print(0)
                                            chance = random.randint(1, 100)
                                            print(1)
                                            print(chance)
                                            if chance > 50:
                                                del_user(id, user)
                                            else:
                                                send_message(id, message='Вам не получилось подставить охотника')
                                        else:
                                            send_message(id, message='У вас не получилось подставить охотника')
                            elif response == '!русская рулетка':
                                rand = random.randint(1, 6)
                                if rand == 3:
                                    send_message(id, message='Прощай')
                                    del_user(id, user_id)
                                else:
                                    send_message(id, message='Вы выжили')
                            elif '!kick' in response:
                                if user_id == '195365002' or user_id == '370633116':
                                    user = str(response[9:18])
                                    del_user(id, user)
    except:
        continue