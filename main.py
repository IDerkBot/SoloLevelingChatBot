from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from datetime import datetime
import calendar
import random
from bs4 import BeautifulSoup as BS
import requests
import pymysql

# Connect to database
conn = pymysql.connect(user='root', host='localhost', db='bot', password='1234', autocommit=True)

# auth with group
token = 'cb7c1219408f725485a7ea95ab23b6767110c0ab1792d249833882b89274a7e5d416aaf71f20c8ffb63a4'
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 195460664)
vk = vk_session.get_api()

def random_anime():
    url = 'https://yummyanime.club/random'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
        'accept': '*/*'}
    r = requests.get(url, headers=HEADERS)
    html = BS(r.content, 'html.parser')
    for el in html.select('.anime-page'):
        title = el.select('h1')
        vk_session.method('messages.send', {'peer_id': event.obj.peer_id, 'message': 'Держи: ' + title[0].text,
                                            'random_id': random.randint(-2147483648, +2147483648)})

def random_animu():
    url = 'https://animego.org/anime/random'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
        'accept': '*/*'}
    r = requests.get(url, headers=HEADERS)
    html = BS(r.content, 'html.parser')
    for el in html.select('.media-body'):
        title = el.select('.anime-title > div > h1')
        print(title)
        vk_session.method('messages.send', {'peer_id': event.obj.peer_id, 'message': 'Держи: ' + title[0].text,
                                            'random_id': random.randint(-2147483648, +2147483648)})

def anime_season():
    season = ''
    print(str(datetime.strftime(datetime.now(), '%m')))
    if (str(datetime.strftime(datetime.now(), '%m')) == '01'):
        season = 'winter'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '02'):
        season = 'winter'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '03'):
        season = 'spring'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '04'):
        season = 'spring'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '05'):
        season = 'spring'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '06'):
        season = 'summer'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '07'):
        season = 'summer'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '08'):
        season = 'summer'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '09'):
        season = 'autumn'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '10'):
        season = 'autumn'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '11'):
        season = 'autumn'
    elif (str(datetime.strftime(datetime.now(), '%m')) == '12'):
        season = 'winter'
    url = 'https://wtf.anilibria.tv/season/' + datetime.strftime(datetime.now(), '%Y') + season + '.html'
    print(url)
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
        'accept': '*/*'}
    message = 'Аниме этого сезона с сайта AniLibria.tv: \n \n'
    r = requests.get(url, headers=HEADERS)
    html = BS(r.content, 'html.parser')
    for el in html.select('.upcoming_float_left'):
        title = el.select('h3')
        message += title[0].text + '\n'
    vk_session.method('messages.send', {'peer_id': event.obj.peer_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})

    # Взять аниме сезона с анилибрии

def top100anime():
    url = 'https://yummyanime.club/top'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
        'accept': '*/*'}
    r = requests.get(url, headers=HEADERS)
    html = BS(r.content, 'html.parser')
    i = 0
    message = 'Вот топ 10 аниме по версии yummyanime.club \n \n'
    for el in html.select('.anime-column'):
        if i < 10: # Кол-во элементов
            i += 1
            title = el.select('.anime-column-info > .anime-title')
            message += '№' + str(i) + ' ' + title[0].text + '\n'
    vk_session.method('messages.send', {'peer_id': event.obj.peer_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})

def top100manga():
    max_page = 5
    pages = []
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
        'accept': '*/*'}
    url = 'https://remanga.org/manga/top-100?ordering=top_pos&count=20&page='
    for x in range(1, max_page + 1):
        pages.append(requests.get(url + str(x), headers=HEADERS))
    i = 0
    message = 'Вот топ 10 манги:\n \n'
    for r in pages:
        html = BS(r.content, 'html.parser')
        for el in html.select('.MuiCardContent-root'):
            if i < 10: # Кол-во элементов
                i += 1
                title = el.select('h4')
                message += '№' + str(i) + ' ' + title[0].text + '\n'
    vk_session.method('messages.send', {'peer_id': event.obj.peer_id, 'message': message,
                                        'random_id': random.randint(-2147483648, +2147483648)})

commands = 'Команды:\n' + '!команды - выводит список всех команд.\n' + \
           '!правила - выводит правила беседы\n' + \
           '!аниме и !аниму - выводят случайным образом название аниме. Это две разные команды построенные на разных алгоритмах.\n' + \
           '!аниме сезона !топ аниме !топ манги - переведены в личные сообщения бота\n' + \
           '!манхва - выводит ссылку на манхву Solo Leveling\n' + \
           '!ранобэ - выводит ссылку на ранобэ Solo Leveling\n' + \
           '!монетка - эмулирует подброс монетки\n' + \
           '!восстань - эмулирует русскую рулетку - Переделано под тематику Solo Leveling\n' + \
           '!последняя глава - выводит ссылку на последнднюю главу манхвы Solo Leveling\n' + \
           '!стата - выводит статистику человека в беседе\n'
commands_admins = 'Команды администрации:\n' + \
           '!статы @id - выводит статистику другого человека\n' + \
           '!повысить [Rank] @id - Повышает или понижает ранг пользователя. В значении [Rank] указывается только одна буква(E, D, C, B, A, S)\n' + \
           '!наградить @id [награда] - выдает пользователю награду, которая отображается в статистике пользователя. В значении [награда] пишется название нагрыды(оно может быть любое)\n' + \
           '!снять награду @id [награда] - убирает у пользователя награду\n'
commands_ls = 'Команды:\n' + \
           '!команды - выводит список всех команд.\n' + \
           '!правила - выводит правила беседы\n' + \
           '!аниме и !аниму - выводят случайным образом название аниме.\n' + \
           '!аниме сезона - выводит аниме которые выходят в этом сезоне\n' + \
           '!топ аниме - выводит топ 100 аниме (список может меняться)\n' + \
           '!топ манги - выводит топ 100 манги (список может меняться)\n' + \
           '!манхва - выводит ссылку на манхву Solo Leveling\n' + \
           '!ранобэ - выводит ссылку на ранобэ Solo Leveling\n' + \
           '!монетка - эмулирует подброс монетки\n' + \
           '!восстань - эмулирует русскую рулетку - Переделано под тематику Solo Leveling\n' + \
           '!последняя глава - выводит ссылку на последнднюю главу манхвы Solo Leveling\n' + \
           '!стата - выводит статистику человека в беседе\n' + \
           '!статы @id - выводит статистику другого человека\n'

with open('rules.txt', 'r') as rul:
    rules = rul.read().splitlines()
rule = 'ПРАВИЛА: \n \n' + rules[1] + '\n' + rules[2] + '\n' + rules[3] + '\n' + rules[4] + '\n' + rules[5]
with open('settings.txt', 'r') as set:
    settings = set.read().splitlines()

link = settings[0]
last_chapter = settings[1]
linkr = settings[2]

setting = [link, last_chapter]

def stats_message():
    sql = "SELECT * FROM `users`"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        rowc = cursor.rowcount
        print(rows)
        print(rowc)
        i = 0
        print(rows[0][1])
        print(rows[0][6])
        humans = ''
        while i < rowc:
            humans += '[id' + str(rows[i][1]) + '|#' + str(i) + ']' + ' сообщений: ' + str(rows[i][6]) + '\n'
            i += 1
        send_message(id, message='Кол-во участников: ' + str(rowc) + '\n' + humans)
def send_message(peer_id, message=None):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})
def del_user(user_id):
    vk_session.method('messages.removeChatUser', {'chat_id': 2000000003, 'user_id': user_id, 'random_id': random.randint(-2147483648, +2147483648)})

print('Bot Active - \033[32mSuccess\033[0m')

# Получение сообщения и ответ
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                id = str(event.obj.peer_id)  # Номер беседы
                user_id = str(event.obj.from_id)
                response = event.obj.text.lower()  # Сообщение из беседы
                print('msg: ' + response)
                print('user: ' + user_id)
                print('group: ' + id)
                time = str(datetime.strftime(datetime.now(), '%H:%M:%S'))
                data = str(datetime.strftime(datetime.now(), '%Y:%m:%d:%H:%M'))
                print(data)
                data = data.split(':')
                print('time: ' + data[2] + '.' + data[1] + '.' + data[0] + ' ' + data[3] + ':' + data[4])
                year = data[0]
                month2 = str(data[1])
                month = str(int(data[1]) + 3)
                day = data[2]
                hour = data[3]
                hour2 = int(data[3]) + 1
                if int(hour2) == 24:
                    hour2 = '00'
                if int(hour2) < 10:
                    hour2 = '0' + str(hour2)
                minute = data[4]
                if month == 13:
                    month = 1
                if month == 14:
                    month = 2
                if month == 15:
                    month = 3
                if int(month) < 10:
                    month = '0' + month
                dataplus = year + ':' + month + ':' + day + ':' + hour + ':' + minute
                print('-' * 30)

                if event.obj.peer_id != event.obj.from_id:

                    with conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + str(event.obj.from_id) + "'")
                        rows = cursor.fetchall()
                        if cursor.rowcount == 0:
                            cursor.execute("INSERT INTO `users` (`uid`, `msg_week`, `msg_all`, `data`) VALUES('" + str(event.obj.from_id) + "', '1', '1', '" + dataplus + "')")
                        else:
                            data_now = data = str(datetime.strftime(datetime.now(), '%Y:%m:%d'))
                            lastmsg = data_now.split(':')
                            date1_str = str(lastmsg[2]) + '.' + str(lastmsg[1]) + '.' + str(lastmsg[0])
                            workdate = datetime.strptime(date1_str, "%d.%m.%Y")
                            str_day = str(calendar.day_abbr[workdate.date().weekday()]).lower()
                            # if str_day.lower() == 'mon':
                            #     print('mon')
                            #     # cursor.execute("SELECT * FROM `users`")
                            #     # rows = cursor.fetchall()
                            #     # rows_c = cursor.rowcount
                            #     # i = 0
                            #     # while i < rows_c:
                            #     #     id_user = rows[i][0]
                            #     #     all_msg = rows[i][7] + 1
                            #     #     cursor.execute("UPDATE `users` SET `msg_week` = '0', `msg_all` = '" + str(all_msg) + "' WHERE (`id` = '" + str(id_user) + "')")
                            #     #     i += 1
                            # else:
                            countmessage = rows[0][6] + 1
                            all_msg = rows[0][7] + 1
                            cursor.execute("UPDATE `users` SET `msg_week` = '" + str(countmessage) + "', `msg_all` = '" + str(all_msg) + "', `data` = '" + dataplus +"' WHERE (`uid` = '" + str(event.obj.from_id) + "')")

                        # Для сообщенией из беседы

                    if response == '!команды':
                        send_message(id, message=commands)
                    elif response == '!admin':
                        send_message(id, message=commands_admins)
                    elif response == '!правила':
                        send_message(id, message=rule)
                    elif response == '!аниме':
                        random_anime()
                    elif response == '!аниму':
                        random_animu()
                    elif response == '!манхва':
                        send_message(id, message='Вот ссылка на манхву: ' + link)
                    elif response == '!ранобэ':
                        send_message(id, message='Вот ссылка на ранобэ: ' + linkr)
                    elif response == '!монетка':
                        value = random.randint(1, 2)
                        if value == 1:
                            send_message(id, message='Орел')
                        elif value == 2:
                            send_message(id, message='Решка')
                    elif response == '!восстань':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                            attemp = rows[0][11]
                        if attemp > 0:
                            value = random.randint(1, 5)
                            if value == 3:
                                with conn.cursor() as cursor:
                                    cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                                    rows = cursor.fetchall()
                                    shadows = str(rows[0][10] + 1)
                                    cursor.execute(
                                        "UPDATE `users` SET `shadows` = '" + shadows + "' WHERE (`uid` = '" + user_id + "')")
                                attemp = 1
                                send_message(id, message='[Призыв тени прошел успешно.]')
                            else:
                                send_message(id, message='[Призыв тени провалился.]')
                            attemp -= 1
                            with conn.cursor() as cursor:
                                cursor.execute(
                                    "UPDATE `users` SET `try` = '" + str(attemp) + "' WHERE (`uid` = '" + user_id + "')")
                        else:
                            send_message(id, message='Количество попыток на сегодня исчерпано')
                    elif response == '!последняя глава':
                        send_message(id, message='Вот ссылка на последнюю главу: ' + last_chapter)
                    elif response == '!число':
                        num = random.randint(0, 1000)
                        send_message(id, message=str(num))
                    elif '!бан' in response:
                        reply = str(event.obj.fwd_messages[0]["from_id"])
                        send_message(id, message='[id' + reply + '|Вы] забанены')
                        # send_message(id, message='К сожалению это команда еще не добавлена, вам повезло')
                    elif response == '!стата' or response == '!статус' or response == '!статистика':
                        sql = "SELECT * FROM `users` WHERE `uid` ='" + str(event.obj.from_id) + "'"
                        with conn.cursor() as cursor:
                            cursor.execute(sql)
                            rows = cursor.fetchall()
                            weekmessage = rows[0][6]
                            ranghunter = '[id' + str(event.obj.from_id) + '|Охотник]'
                            shadows = str(rows[0][10])
                            if str(rows[0][2]) == '1':
                                name = 'E - ранга'
                            elif str(rows[0][2]) == '2':
                                name = 'D - ранга'
                            elif str(rows[0][2]) == '3':
                                name = 'C - ранга'
                            elif str(rows[0][2]) == '4':
                                name = 'B - ранга'
                            elif str(rows[0][2]) == '5':
                                name = 'A - ранга'
                            elif str(rows[0][2]) == '6':
                                name = 'S - ранга'
                            elif str(rows[0][2]) == '7':
                                name = 'Национального уровня'
                            send_message(id, message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(weekmessage) + '\n Награды: ' + rows[0][3].capitalize())
                    elif '!статы' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            reply = str(event.obj.fwd_messages[0]["from_id"])
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + reply + "'")
                                rows = cursor.fetchall()
                                weekmessage = rows[0][6]
                                ranghunter = '[id' + reply + '|Охотник]'
                                shadows = str(rows[0][10])
                                if str(rows[0][2]) == '1':
                                    name = 'E - ранга'
                                elif str(rows[0][2]) == '2':
                                    name = 'D - ранга'
                                elif str(rows[0][2]) == '3':
                                    name = 'C - ранга'
                                elif str(rows[0][2]) == '4':
                                    name = 'B - ранга'
                                elif str(rows[0][2]) == '5':
                                    name = 'A - ранга'
                                elif str(rows[0][2]) == '6':
                                    name = 'S - ранга'
                                elif str(rows[0][2]) == '7':
                                    name = 'Национального уровня'
                                send_message(id, message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(weekmessage) + '\n Награды: ' + rows[0][3].capitalize())
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                    elif response == '!топ':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` ORDER BY `shadows` DESC")
                                rows = cursor.fetchall()
                            i = 0
                            top = ''
                            while i < 5:
                                top += '[id' + str(rows[i][1]) + '|#' + str(i+1) + '] - теней: ' + str(rows[i][10]) + '\n'
                                i += 1
                            send_message(id, message=top)
                        else:
                            send_message(id, message='У вас нет прав для этой команды')
                    elif response == '!tmsg':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` ORDER BY `msg_week` DESC")
                                rows = cursor.fetchall()
                            i = 0
                            msg = ''
                            while i < 5:
                                msg += '[id' + str(rows[i][1]) + '|#' + str(i+1) + '] - сообщений: ' + str(rows[i][6]) + '\n'
                                i += 1
                            send_message(id, message=msg)
                    # elif response == '!насилие':
                    #     send_message(id, message='[id' + str(event.obj.from_id) + '|Ты] был изнасилован')
                    elif '!повысить' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            rang = str(response[10:len(response)])
                            reply = str(event.obj.fwd_messages[0]["from_id"])
                            if rang.lower() == 'e':
                                sql = "UPDATE `users` SET `level` = '1' WHERE (`uid` = '" + reply + "')"
                                name = 'E - ранга'
                            if rang.lower() == 'd':
                                sql = "UPDATE `users` SET `level` = '2' WHERE (`uid` = '" + reply + "')"
                                name = 'D - ранга'
                            elif rang.lower() == 'c':
                                sql = "UPDATE `users` SET `level` = '3' WHERE (`uid` = '" + reply + "')"
                                name = 'C - ранга'
                            elif rang.lower() == 'b':
                                sql = "UPDATE `users` SET `level` = '4' WHERE (`uid` = '" + reply + "')"
                                name = 'B - ранга'
                            elif rang.lower() == 'a':
                                sql = "UPDATE `users` SET `level` = '5' WHERE (`uid` = '" + reply + "')"
                                name = 'A - ранга'
                            elif rang.lower() == 's':
                                sql = "UPDATE `users` SET `level` = '6' WHERE (`uid` = '" + reply + "')"
                                name = 'S - ранга'
                            elif rang.lower() == 'sss':
                                sql = "UPDATE `users` SET `level` = '7' WHERE (`uid` = '" + reply + "')"
                                name = 'Национального уровня'
                            with conn.cursor() as cursor:
                                cursor.execute(sql)
                            send_message(id, message='[id' + reply + '|Вы] были повышены до ' + name)
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                    elif '!наградить' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            reply = str(event.obj.fwd_messages[0]["from_id"])
                            print(reply)
                            achivment = response[11:len(response)]
                            print(achivment)
                            with conn.cursor() as cursor:
                                print(0)
                                cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + reply + "'")
                                print(1)
                                rows = cursor.fetchall()
                                print(2)
                                if rows[0][3] == 'none':
                                    print(3)
                                    achivment = achivment
                                    print(4)
                                else:
                                    print(5)
                                    achivment = rows[0][3] + ', ' + achivment
                                    print(6)
                                print(7)
                                cursor.execute("UPDATE `users` SET `achivment` = '" + achivment + "' WHERE (`uid` = '" + reply + "')")
                                print(10)
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                    elif '!снять награду' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            achivment = response[18:len(response)]
                            user = achivment[0:9]
                            end = achivment.index('] ', 0, len(achivment))
                            end += 2
                            achivment = achivment[end:len(achivment)]
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + user + "'")
                                rows = cursor.fetchall()
                                if rows[0][3] == 'none':
                                    send_message(id, message='У охотника нет наград!')
                                else:
                                    row = rows[0][3]
                                    row.split(',')
                                    row = row.lower()
                                    achivst = row.index(achivment, 0, len(row))
                                    if achivst != 0:
                                        achivst -= 2
                                        achivend = achivst + 2 + len(achivment)
                                    else:
                                        achivend = achivst + len(achivment)
                                    achivend += 2
                                    achivment = row[0:achivst] + row[achivend:len(row)]
                                    sql = "UPDATE `users` SET `achivment` = '" + achivment + "' WHERE (`uid` = '" + user + "')"
                            with conn.cursor() as cursor:
                                cursor.execute(sql)
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                    elif '!stat' in response:
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user_id + "'")
                            rows = cursor.fetchall()
                        if int(rows[0][2]) >= 4:
                            stats_message()
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                # Команды для ЛС бота
                if event.obj.peer_id == event.obj.from_id:
                    if response == '!команды':
                        send_message(id, message=commands_ls)
                    elif response == '!стата':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + id + "'")
                            rows = cursor.fetchall()
                            weekmessage = rows[0][6]
                            ranghunter = '[id' + id + '|Охотник]'
                            shadows = str(rows[0][10])
                            if str(rows[0][2]) == '1':
                                name = 'E - ранга'
                            elif str(rows[0][2]) == '2':
                                name = 'D - ранга'
                            elif str(rows[0][2]) == '3':
                                name = 'C - ранга'
                            elif str(rows[0][2]) == '4':
                                name = 'B - ранга'
                            elif str(rows[0][2]) == '5':
                                name = 'A - ранга'
                            elif str(rows[0][2]) == '6':
                                name = 'S - ранга'
                            elif str(rows[0][2]) == '7':
                                name = 'Национального уровня'
                            send_message(id,
                                         message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(
                                             weekmessage) + '\n Награды: ' + rows[0][3].capitalize())
                    elif response == '!правила':
                        send_message(id, message=rule)
                    elif response == '!восстань':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + id + "'")
                            rows = cursor.fetchall()
                            attemp = rows[0][11]
                        if attemp > 0:
                            value = random.randint(1, 5)
                            if value == 3:
                                with conn.cursor() as cursor:
                                    cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + id + "'")
                                    rows = cursor.fetchall()
                                    shadows = str(rows[0][10] + 1)
                                    cursor.execute(
                                        "UPDATE `users` SET `shadows` = '" + shadows + "' WHERE (`uid` = '" + id + "')")
                                send_message(id, message='[Призыв тени прошел успешно.]')
                            else:
                                send_message(id, message='[Призыв тени провалился.]')
                            attemp -= 1
                            with conn.cursor() as cursor:
                                cursor.execute(
                                    "UPDATE `users` SET `try` = '" + str(attemp) + "' WHERE (`uid` = '" + id + "')")
                        else:
                            send_message(id, message='Количество попыток на сегодня исчерпано')
                    elif '!статы' in response:
                        stats = response[7:len(response)]
                        users = stats[3:12]
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + users + "'")
                            rows = cursor.fetchall()
                            weekmessage = rows[0][6]
                            ranghunter = '[id' + users + '|Охотник]'
                            shadows = str(rows[0][10])
                            if str(rows[0][2]) == '1':
                                name = 'E - ранга'
                            elif str(rows[0][2]) == '2':
                                name = 'D - ранга'
                            elif str(rows[0][2]) == '3':
                                name = 'C - ранга'
                            elif str(rows[0][2]) == '4':
                                name = 'B - ранга'
                            elif str(rows[0][2]) == '5':
                                name = 'A - ранга'
                            elif str(rows[0][2]) == '6':
                                name = 'S - ранга'
                            elif str(rows[0][2]) == '7':
                                name = 'Национального уровня'
                        send_message(id,
                                         message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(
                                             weekmessage) + '\n Награды: ' + rows[0][3].capitalize())
                    elif response == '!аниме':
                        random_anime()
                    elif response == '!аниму':
                        random_animu()
                    elif response == '!топ':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` ORDER BY `shadows` DESC")
                            rows = cursor.fetchall()
                        i = 0
                        top = ''
                        while i < 5:
                            top += '[id' + str(rows[i][1]) + '|#' + str(i + 1) + '] - теней: ' + str(rows[i][10]) + '\n'
                            i += 1
                        send_message(id, message=top)
                    elif response == '!tmsg':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` ORDER BY `msg_week` DESC")
                            rows = cursor.fetchall()
                        i = 0
                        msg = ''
                        while i < 5:
                            msg += '[id' + str(rows[i][1]) + '|#' + str(i + 1) + '] - сообщений: ' + str(
                                rows[i][6]) + '\n'
                            i += 1
                        send_message(id, message=msg)
                    elif response == '!аниме сезона':
                        anime_season()
                    elif response == '!топ аниме':
                        top100anime()
                    elif response == '!топ манги':
                        top100manga()
                    elif response == '!последняя глава':
                        send_message(id, message='Вот ссылка на последнюю главу: ' + last_chapter)
                    elif response == '!манхва':
                        send_message(id, message='Вот ссылка на манхву: ' + link)
                    elif response == '!ранобэ':
                        send_message(id, message='Вот ссылка на ранобэ: ' + linkr)
                    elif '!важно' in response:
                        if id == '370633116' or id == '195365002':
                            warning = response[6:len(response)]
                            send_message(2000000004, 'Важная информация:\n' + warning.capitalize())
                            send_message(id, message='Информация отправлена')
                        else:
                            send_message(id, message='У вас нет доступа к этой команде!')

                    elif '!link edit' in response:
                        if id == '370633116' or id == '195365002':
                            relink = response[11:len(response)]
                            setting[0] = relink
                            with open(r'settings.txt', 'w')as f:
                                for line in setting:
                                    f.write(line + '\n')
                                send_message(id, message='Ссылка на манхву изменена')
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')

                    elif '!chapter edit' in response:
                        if id == '370633116' or id == '195365002':
                            rechapter = response[14:len(response)]
                            setting[1] = rechapter
                            with open(r'settings.txt', 'w')as f:
                                for line in setting:
                                    f.write(line + '\n')
                                send_message(id, message='Ссылка на последнюю главу изменена')
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')
                    elif '!update' == response:
                        if id == '370633116' or id == '195365002':
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` WHERE `try` = '0'")
                                rows = cursor.fetchall()
                                rows_c = cursor.rowcount
                            i = 0
                            while i < rows_c:
                                id_user = rows[i][0]
                                with conn.cursor() as cursor:
                                    cursor.execute(
                                        "UPDATE `users` SET `try` = '3' WHERE (`id` = '" + str(id_user) + "')")
                                i += 1
                            send_message(2000000004, message='Количество попыток обновилено')
                            send_message(id, message='Кол-во попыток обновлено')
                        else:
                            send_message(id, message='У вас нет прав для этой команды!')


                # Приветствие пользователя когда он вступил в беседу
                if event.obj.action["type"] == 'chat_invite_user':
                    fullname = '[id' + str(event.obj.action["member_id"]) + '|охотник]'
                    send_message(id, message='Добро пожаловать ' + fullname + ' \n Для ознакомления с правилами напишите - !правила ')
                if event.obj.action["type"] == 'chat_kick_user':
                    fullname = '[id' + str(event.obj.action["member_id"]) + '|Охотник]'
                    with conn.cursor() as cursor:
                        cursor.execute("DELETE FROM `users` WHERE (`uid` = '" + str(event.obj.action["member_id"]) + "')")
                    send_message(id, message=fullname + ' пал в подземелье')
    except:
        continue