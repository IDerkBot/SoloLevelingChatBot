from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import pymysql.cursors
import random
from bs4 import BeautifulSoup as BS
import datetime
import requests

conn = pymysql.connect(user='root', host='localhost', db='bot', password='1234', autocommit=True)

token = 'cb7c1219408f725485a7ea95ab23b6767110c0ab1792d249833882b89274a7e5d416aaf71f20c8ffb63a4'
vk_session = vk_api.VkApi(token=token)
vk_session._auth_token()
longpoll = VkLongPoll(vk_session)
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
        send_message(user, 'Держи: ' + title[0].text)

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
        send_message(user, message='Держи: ' + title[0].text)

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
    send_message(user, message=message)

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
    send_message(user, message=message)

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
    send_message(user, message=message)

with open('rules.txt', 'r') as rul:
    rules = rul.read().splitlines()
rule = 'ПРАВИЛА: \n \n' + rules[1] + '\n' + rules[2] + '\n' + rules[3] + '\n' + rules[4] + '\n' + rules[5] + '\n \n' +\
       'Кто нарушит правила, того кикаем из беседы, в редких случаях из ГРУППЫ!!!' +\
       '\n В случае нарушения правил сообщаем:\n https://vk.com/id370633116\n https://vk.com/loverre\n https://vk.com/yazplay\n https://vk.com/id409784302'

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
        i = 0
        humans = ''
        while i < rowc:
            humans += '[id' + str(rows[i][1]) + '|#' + str(i) + ']' + ' сообщений: ' + str(rows[i][6]) + '\n'
            i += 1
        send_message(user, message='Кол-во участников: ' + str(rowc) + '\n' + humans)

commands = 'Команды:\n' + \
           '!команды - выводит список всех команд.\n' + \
           '!правила - выводит правила беседы\n' + \
           '!аниме и !аниму - выводят случайным образом название аниме. Это две разные команды построенные на разных алгоритмах.\n' + \
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


def send_message(peer_id, message=None):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})

print('Bot Active - \033[32mSuccess\033[0m')

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                user = str(event.user_id)
                response = event.text.lower()
                print('user: ' + user)
                print('message: ' + response)

                if response == '!стата':
                    with conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user + "'")
                        rows = cursor.fetchall()
                        weekmessage = rows[0][6]
                        ranghunter = '[id' + user + '|Охотник]'
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
                        send_message(user, message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(
                            weekmessage) + '\n Награды: ' + rows[0][3].capitalize())
                elif response == '!команды':
                    send_message(user, message=commands)
                elif response == '!правила':
                    send_message(user, message=rule)
                elif response == '!восстань':
                    with conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user + "'")
                        rows = cursor.fetchall()
                        attemp = rows[0][11]
                    if attemp > 0:
                        value = random.randint(1, 5)
                        if value == 3:
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT * FROM `users` WHERE `uid` = '" + user + "'")
                                rows = cursor.fetchall()
                                shadows = str(rows[0][10] + 1)
                                cursor.execute(
                                    "UPDATE `users` SET `shadows` = '" + shadows + "' WHERE (`uid` = '" + user + "')")
                            send_message(user, message='[Призыв тени прошел успешно.]')
                        else:
                            send_message(user, message='[Призыв тени провалился.]')
                        attemp -= 1
                        with conn.cursor() as cursor:
                            cursor.execute("UPDATE `users` SET `try` = '" + str(attemp) + "' WHERE (`uid` = '" + user + "')")
                    else:
                        send_message(user, message='Количество попыток на сегодня исчерпано')

                elif response == '!монетка':
                    value = random.randint(1, 2)
                    if value == 1:
                        send_message(user, message='Орел')
                    elif value == 2:
                        send_message(user, message='Решка')
                elif '!статы' in response:
                    stats = response[7:len(response)]
                    users = stats[3:12]
                    with conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + users + "'")
                        rows = cursor.fetchall()
                        weekmessage = rows[0][6]
                        ranghunter = '[id' + user + '|Охотник]'
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
                    send_message(user, message=ranghunter + ': ' + name + '\n Количество теней: ' + shadows + ' \n Сообщений за эту неделю: ' + str(
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
                    send_message(user, message=top)
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
                    send_message(user, message=msg)
                elif response == '!аниме сезона':
                    anime_season()
                elif response == '!топ аниме':
                    top100anime()
                elif response == '!топ манги':
                    top100manga()
                elif response == '!последняя глава':
                    send_message(user, message='Вот ссылка на последнюю главу: ' + last_chapter)
                # elif '!число' in response:
                #     number = response[7:len(response)]
                #     randoms = random.randint(0, 100)
                #     if int(number) > randoms:
                #         send_message(user, message=number + '>' + randoms)
                #     elif int(number) < randoms:
                #         send_message(user, message=number + '<' + randoms)
                #     elif int(number) == randoms:
                #         send_message(user, message=number + '=' + randoms)
                elif response == '!манхва':
                    send_message(user, message='Вот ссылка на манхву: ' + link)
                elif response == '!ранобэ':
                    send_message(user, message='Вот ссылка на ранобэ: ' + linkr)
                elif response == '!stat':
                    if user == '370633116' or user == '195365002':
                        stats_message()
                    else:
                        send_message(user, message='У вас нет доступа к этой команде!')

                elif '!важно' in response:
                    if user == '370633116' or user == '195365002':
                        warning = response[6:len(response)] # Solo leveling - 2000000004 # Ассоциация - 2000000003
                        send_message(2000000004, 'Важная информация:\n' + warning.capitalize())
                        send_message(user, message='Информация отправлена')
                    else:
                        send_message(user, message='У вас нет доступа к этой команде!')

                elif '!link edit' in response:
                    if user == '370633116' or user == '195365002':
                        relink = event.obj.text
                        relink = relink[11:len(relink)]
                        setting[0] = relink
                        with open(r'settings.txt', 'w')as f:
                            for line in setting:
                                f.write(line + '\n')
                            send_message(user, message='Ссылка на манхву изменена')
                    else:
                        send_message(user, message='У вас нет прав для этой команды!')

                elif '!chapter edit' in response:
                    if user == '370633116' or user == '195365002':
                        rechapter = event.obj.text
                        rechapter = rechapter[14:len(rechapter)]
                        setting[1] = rechapter
                        with open(r'settings.txt', 'w')as f:
                            for line in setting:
                                f.write(line + '\n')
                            send_message(user, message='Ссылка на последнюю главу изменена')
                    else:
                        send_message(user, message='У вас нет прав для этой команды!')
                elif '!update' == response:
                    if user == '370633116' or user == '195365002':
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `try` = '0'")
                            rows = cursor.fetchall()
                            rows_c = cursor.rowcount
                        i = 0
                        while i < rows_c:
                            id_user = rows[i][0]
                            with conn.cursor() as cursor:
                                cursor.execute("UPDATE `users` SET `try` = '3' WHERE (`id` = '" + str(id_user) + "')")
                            i += 1
                        send_message(2000000004, message='Кол-во попыток обновилось')
                    else:
                        send_message(user, message='У вас нет прав для этой команды!')

    except:
        continue