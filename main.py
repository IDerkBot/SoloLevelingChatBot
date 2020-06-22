from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from datetime import datetime
import calendar
import random
from bs4 import BeautifulSoup as BS
import requests
import pymysql
from vk_api.upload import VkUpload

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
        send_message(id, message='Держи: ' + title[0].text)
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
        send_message(id, message='Держи: ' + title[0].text)
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
    send_message(id, message=message)

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
    send_message(id, message=message)
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
    send_message(id, message=message)

commands = 'Команды:\n' + '!команды - выводит список всех команд.\n' + \
           '!правила - выводит правила беседы\n' + \
           '!аниме и !аниму - выводят случайным образом название аниме. Это две разные команды построенные на разных алгоритмах.\n' + \
           '!манхва - выводит ссылку на манхву Solo Leveling\n' + \
           '!ранобэ - выводит ссылку на ранобэ Solo Leveling\n' + \
           '!монетка - эмулирует подброс монетки\n' + \
           '!последняя глава - выводит ссылку на последнднюю главу манхвы Solo Leveling\n' + \
           '!стата - выводит статистику человека в беседе\n' + \
           '!бой - предложение участнику сразится в бое на тенях\n' + \
           '!принять - принимает предложение на бой\n' + \
           '!отклонить - отклоняет предложение на бой\n' + \
           '!дать тени $ - передает тени выбраному участнику (заместо "$" ставится число)\n' + \
           '!кости ($) - эмулирует бросок костей, максимально кол-во костей = 5\n' + \
           '!ник $ - смена ника\n' + \
           '!преды - показывает кол-во выданных предупреждений\n'
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

rules = '1.1 Не оскорбляем!\n' + '1.2 Не создаем ссоры!\n' + '1.3 Не дезинформируем!\n' + \
        '2. Не кидаем контент откровенного характера! (Хентай, порнография и т.д.)\n' + \
        '3. Не спамим и не флудим!\n' + \
        '4. Спойлеры запрещены по любому произведению! Если хотите проспойлерить сюжет, то переходите в личку собеседника\n' + \
        '5. Запрещено использование команд all и online\n' + '6. Багоюз'
with open('settings.txt', 'r') as set:
    settings = set.read().splitlines()

link = settings[0]
last_chapter = settings[1]
linkr = settings[2]
setting = [link, last_chapter]

def arise():
    data = d_user(from_id)
    attemp = data['try']
    if attemp > 0:
        i = 1
        shad = 0
        message = ''
        while i <= 3 and shad == 0:
            chance = random.randint(1, 3)
            if chance == 3:
                shadows = str(data['shadows'] + 1)
                update_db('users', 'shadows', shadows, from_id)
                shad = 1
                message += '[Призыв тени прошел успешно.]\n'
            else:
                message += '[Призыв тени провалился.]\n'
            i += 1
        attemp -= 1
        update_db('users', 'try', str(attemp), from_id)
        send_message(id, message=message)
    else:
        send_message(id, message='Количество попыток на сегодня исчерпано')
def access():
    data = d_user(from_id)
    access_key = 0
    if data['rang'] == 4: # B
        access_key = 1
    elif data['rang'] == 5: # A
        access_key = 2
    elif data['rang'] == 6: # S
        access_key = 3
    elif data['rang'] == 7: # SSS
        access_key = 4
    elif data['rang'] == 8: # I
        access_key = 5
    elif data['rang'] == 0: # Human
        access_key = 3
    return access_key
def accept():
    data = d_user(from_id)
    h1_uid = data['uid']
    h1_shadows = data['shadows']
    h1_win = data['win']
    h1_lose = data['lose']
    if h1_shadows <= 0:
        update_db('users', 'fight', 'none', h1_uid)
        send_message(id, message='У вас нет теней для боя')
        pass
    h2_uid = data['fight']
    if h2_uid == 'none':
        send_message(id, message='Вам никто не бросал вызов')
    else:
        data2 = d_user(h2_uid)
        h2_shadows = data2['shadows']
        if h2_shadows <= 0:
            update_db('users', 'fight', 'none', h1_uid)
            send_message(id, message='У вашего противника нет теней для боя')
        else:
            h2_win = data2['win']
            h2_lose = data2['lose']
            rand = random.randint(1, 100)
            all_shadows = h1_shadows + h2_shadows
            h1_percent = round(int(h1_shadows) / int(all_shadows) * 100, 1)
            h2_percent = round(int(h2_shadows) / int(all_shadows) * 100, 1)
            user1 = vk_session.method("users.get", {"user_ids": h1_uid})
            h1_name = '[id' + h1_uid + '|' + user1[0]['first_name'] + ']'
            user2 = vk_session.method("users.get", {"user_ids": h2_uid})
            h2_name = '[id' + h2_uid + '|' + user2[0]['first_name'] + ']'
            send_message(id, message='Шансы:\n' + h1_name + ' - ' + str(h1_percent) + '%' + '\n' + h2_name + ' - ' + str(h2_percent) + '%')
            if rand <= h1_percent:
                send_message(id, message='Победил [id' + h1_uid + '|охотник]')
                h1_shadows += 1
                h2_shadows -= 1
                h1_win += 1
                h2_lose += 1
                update_db('users', 'shadows', str(h1_shadows), h1_uid)
                update_db('users', 'fight', 'none', h1_uid)
                update_db('users', 'win', str(h1_win), h1_uid)
                update_db('users', 'shadows', str(h2_shadows), h2_uid)
                update_db('users', 'fight', 'none', h2_uid)
                update_db('users', 'lose', str(h2_lose), h2_uid)
            else:
                send_message(id, message='Победил [id' + h2_uid + '|охотник]')
                h1_shadows -= 1
                h2_shadows += 1
                h2_win += 1
                h1_lose += 1
                update_db('users', 'shadows', str(h1_shadows), h1_uid)
                update_db('users', 'fight', 'none', h1_uid)
                update_db('users', 'lose', str(h1_lose), h1_uid)
                update_db('users', 'shadows', str(h2_shadows), h2_uid)
                update_db('users', 'fight', 'none', h2_uid)
                update_db('users', 'win', str(h2_win), h2_uid)
def boss():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `boss`")
        rowc = cursor.rowcount
    i = 0
    while i <= rowc:

        i += 1
    pass
    # data = d_user(from_id)
    # if data['shadows'] <= 0:
    #     send_message(id, message='Вы не можете бросить вызов, у вас нет теней')
    # elif data['boss'] == 0:
    #     send_message(id, message='[id' + from_id + '|Вы] бросили вызов боссу')
    #     h1_uid = str(data['uid'])
    #     h1_shadows = data['shadows']
    #     data2 = d_user('195365002')
    #     h2_shadows = data2['shadows']
    #     rand = random.randint(0, 100)
    #     all_shadows = h1_shadows + h2_shadows
    #     h1_percent = round(int(h1_shadows) / int(all_shadows) * 100, 1)
    #     h2_percent = round(int(h2_shadows) / int(all_shadows) * 100, 1)
    #     h1_name = '[id' + h1_uid + '|Охотник]'
    #     send_message(id, message='Шансы:\n' + h1_name + ' - ' + str(
    #         h1_percent) + '%' + '\n[Кроваво-красный полководец Игрис] - ' + str(h2_percent) + '%')
    #     if rand <= h1_percent:
    #         send_message(id, message='Победил [id' + h1_uid + '|охотник]')
    #         h1_shadows += 10
    #         update_db('users', 'shadows', str(h1_shadows), h1_uid)
    #         update_db('users', 'boss', '1', h1_uid)
    #     else:
    #         send_message(id, message='Победил [Кроваво-красный полководец Игрис]')
    #         h1_shadows -= 1
    #         update_db('users', 'shadows', str(h1_shadows), h1_uid)
    # elif data['boss'] == 1:
    #     send_message(id, message='[id' + from_id + '|Вы] уже одолели босса!')
def bones(count):
    if count == '1' or count == '':
        count = 1
    elif count == '2':
        count = 2
    elif count == '3':
        count = 3
    elif count == '4':
        count = 4
    elif count == '5':
        count = 5
    i = 1
    all = 0
    message = 'Выпало:'
    while i <= count:
        drop = random.randint(1, 6)
        all += drop
        message += ' ' + str(drop)
        i += 1
    send_message(id, message=message + '\nОчков выпало: ' + str(all))
    pass

def buy(type_buy):
    pass

def complains(user_id):
    data = d_user(user_id)
    complain = data['complain']
    complain += 1
    update_db('users', 'complain', str(complain), user_id)
    reason = response[6:len(response)]
    start = 'Выдано предупреждение ' + str(complain) + '/3\nПричина: '
    midle = ''
    if reason == '1.1':
        midle = 'Оскорбление'
    elif reason == '1.2':
        midle = 'Ссора'
    elif reason == '1.3':
        midle = 'Дезинформация'
    elif reason == '2':
        midle = 'Контент откровенного характера'
    elif reason == '3':
        midle = 'Спам или флуд'
    elif reason == '4':
        midle = 'Спойлеры'
    elif reason == '5':
        midle = 'Использование команд @ all или online'
    elif reason == '6':
        midle = 'Багоюз'
    send_message(id, message=start + midle)
def coin():
    value = random.randint(1, 2)
    if value == 1: send_message(id, message='Орел')
    elif value == 2: send_message(id, message='Решка')
def set_achievement(user):
    achievement = response[11:len(response)]
    data = d_user(user)
    if data['achievement'] == 'none':
        achievement = achievement
    else:
        achievement = data['achievement'] + ', ' + achievement
    update_db('users', 'achievement', achievement, user)
def del_achievement(user, achievement):
    data = d_user(user)
    if data['achievement'] == 'none':
        send_message(id, message='У охотника нет наград!')
        none_achievement = 'asdzxc'
        return none_achievement
    else:
        row = rows[0][4]
        row.split(',')
        row = row.lower()
        achivst = row.index(achievement, 0, len(row))
        if achivst != 0:
            achivst -= 2
            achivend = achivst + 2 + len(achievement)
        else:
            achivend = achivst + len(achievement)
        achivend += 2
        achievement = row[0:achivst] + row[achivend:len(row)]
        update_db('users', 'achievement', achievement, user)
        data = d_user(user)
        if data['achievement'] == '':
            update_db('users', 'achievement', 'none', user)
        send_message(id, message='Награда успешна снята')
def d_user(user_id):
    with conn.cursor() as cursor:
        cursor.execute("select * from `users` where `uid` = '" + user_id + "'")
        rows = cursor.fetchall()
    dict = {'id': rows[0][0], 'uid': rows[0][1], 'nick': rows[0][2], 'rang': rows[0][3], 'achievement': rows[0][4],
            'msg_week': rows[0][5], 'msg_all': rows[0][6], 'data': rows[0][7], 'shadows': rows[0][8], 'try': rows[0][9],
            'fight': rows[0][10], 'win': rows[0][11], 'lose': rows[0][12], 'boss': rows[0][13], 'complain': rows[0][14], 'invis': rows[0][15]}
    return dict
def give_shadows():
    num = str(response[11:len(response)])
    if int(num) >= 0:
        reply = str(event.obj.fwd_messages[0]["from_id"])
        data = d_user(from_id)
        if data['shadows'] == 0:
            send_message(id, message='У вас нет теней для передачи')
        elif data['shadows'] > 0:
            if int(num) > data['shadows']:
                send_message(id, message='Вы пытаетесь передать слишком много теней')
            else:
                count_shadows = data['shadows'] - int(num)
                update_db('users', 'shadows', str(count_shadows), from_id)
                data2 = d_user(reply)
                count_shadows2 = data2['shadows'] + int(num)
                update_db('users', 'shadows', str(count_shadows2), reply)
                send_message(id, message='Тени переданы')
    else:
        send_message(id, message='Баг пофиксили!')
def steal():
    num = str(response[9:len(response)])
    if int(num) >= 0:
        reply = str(event.obj.fwd_messages[0]["from_id"])
        data = d_user(from_id)
        if data['shadows'] == 0:
            send_message(id, message='У охотника нет теней')
        elif data['shadows'] > 0:
            if int(num) > data['shadows']:
                send_message(id, message='Вы пытаетесь украсть слишком много теней')
            else:
                count_shadows = data['shadows'] + int(num)
                update_db('users', 'shadows', str(count_shadows), from_id)
                data2 = d_user(reply)
                count_shadows2 = data2['shadows'] - int(num)
                update_db('users', 'shadows', str(count_shadows2), reply)
                send_message(id, message='Тени украдены')
def lvl_up(from_in, from_out):
    rang = str(response[10:len(response)])
    if from_in != from_out:
        if rang == 'e':
            name = 'E - ранга'
            rang_int = 1
        elif rang == 'd':
            name = 'D - ранга'
            rang_int = 2
        elif rang == 'c':
            name = 'C - ранга'
            rang_int = 3
        elif rang == 'b':
            name = 'B - ранга'
            rang_int = 4
        elif rang == 'a':
            name = 'A - ранга'
            rang_int = 5
        elif rang == 's':
            name = 'S - ранга'
            rang_int = 6
        elif rang == 'sss':
            name = 'Национального уровня'
            rang_int = 7
        update_db('users', 'rang', str(rang_int), from_out)
        send_message(id, message='[id' + from_out + '|Вы] были повышены до ' + name)
    else:
        send_message(id, message='Вы не можете повысить самого себя')
def nickname():
    nick = response[5:len(response)]
    if nick == '':
        send_message(id, message='Пожалуйста введите корректный ник')
    elif nick == '.!.':
        send_message(id, message='Бан')
    else:
        update_db('users', 'nickname', nick, from_id)
        send_message(id, message='Ник успешно изменен')
def send_message(peer_id, message=None):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})
def shop():
    pass
def stats_message():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `users`")
        rowc = cursor.rowcount
    i = 0
    while i < rowc:
        i += 1
    send_message(id, message='Кол-во участников: ' + str(rowc) + '\n')
def status(type_user):
    stat = d_user(type_user)
    msg_week = str(stat['msg_week'])
    hunter = '[id' + type_user + '|Охотник]'
    h_nick = stat['nick'].capitalize()
    h_shadows = str(stat['shadows'])
    h_rang = str(stat['rang'])
    h_achievement = stat['achievement'].capitalize()
    if h_rang == '0':
        hunter = '[id' + type_user + '|Простолюдин]'
        rang_l = ''
    elif h_rang == '1':
        rang_l = 'E - ранга'
    elif h_rang == '2':
        rang_l = 'D - ранга'
    elif h_rang == '3':
        rang_l = 'C - ранга'
    elif h_rang == '4':
        rang_l = 'B - ранга'
    elif h_rang == '5':
        rang_l = 'A - ранга'
    elif h_rang == '6':
        rang_l = 'S - ранга'
    elif h_rang == '7':
        rang_l = 'Национального уровня'
    if type_user == '-195460664':
        send_message(id, message='[public195460664|Ассоциация]' + '\n Количество теней: 10000000\n')
    else:
        if stat['invis'] == 0:
            send_message(id,
                     message=hunter + ': ' + rang_l + '\n Ник: ' + h_nick + '\n Количество теней: ' + h_shadows +
                             '\n Сообщений за эту неделю: ' + msg_week + '\n Награды: ' + h_achievement +
                     '\n Побед: ' + str(stat['win']) + '\n Поражений: ' + str(stat['lose']))
        elif stat['invis'] == 1 and from_id != type_user:
            send_message(id, message='Охотник скрыл свои данные')
        elif stat['invis'] == 1 and from_id == type_user:
            if h_rang == '8':
                send_message(id, message='[id' + type_user + '|Апокалипсис]\nДемоны которым писать о проблемах:\n'
                                                         '1. [id222404660|Михаил Домнич](Смерть)\n'
                                                         '2. [id127789804|Николай Кривонос](Война)\n'
                                                         '3. [id248168270|Сметанка](Голод)\n'
                                                         '4. [id196873187|Ксения Афанасьева](Чума)')
            else:
                send_message(id,
                             message=hunter + ': ' + rang_l + '\n Ник: ' + h_nick + '\n Количество теней: ' + h_shadows +
                                     '\n Сообщений за эту неделю: ' + msg_week + '\n Награды: ' + h_achievement +
                                     '\n Побед: ' + str(stat['win']) + '\n Поражений: ' + str(stat['lose']))
def top_msg():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `users` ORDER BY `msg_week` DESC")
        rows = cursor.fetchall()
    i = 0
    msg = ''
    while i < 5:
        msg += '[id' + str(rows[i][1]) + '|#' + str(i + 1) + '] - сообщений: ' + str(rows[i][5]) + '\n'
        i += 1
    send_message(id, message=msg)
def top_shadows():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `users` ORDER BY `shadows` DESC")
        rows = cursor.fetchall()
    i = 1
    top = ''
    while i < 6:
        top += '[id' + str(rows[i][1]) + '|#' + str(i) + '] - теней: ' + str(rows[i][8]) + '\n'
        i += 1
    send_message(id, message=top)
def prize(count):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `users`")
        rows = cursor.fetchall()
        rowc = cursor.rowcount
    i = 0
    message = ''
    while i < 5:
        human = random.randint(1, rowc)
        print(rows[human])
        uid = rows[human][1]
        shadows = rows[human][8]
        shadows += int(count)
        update_db('users', 'shadows', str(shadows), uid)
        message += '[id' + uid + '|Победитель!]\n'
        i += 1
    send_message(id, message=message)

def update_db(table, column, value, who):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE `" + table + "` SET `" + column + "` = '" + value + "' WHERE(`uid` = '" + who + "')")

print('Bot Active - \033[32mSuccess\033[0m')

# Получение сообщения и ответ
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                id = str(event.obj.peer_id)  # Номер беседы
                from_id = str(event.obj.from_id)
                response = event.obj.text.lower()  # Сообщение из беседы
                user = vk_session.method("users.get", {"user_ids": from_id})  # Имя и Фамилия пользователя
                fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
                if str(event.obj.attachments) != '[]':
                    print('photo: ' + event.obj.attachments[0]['photo']['sizes'][3]['url'])
                print('msg: ' + response)
                print('name: ' + fullname)
                print('user: ' + from_id)
                print('group: ' + id)
                data = str(datetime.strftime(datetime.now(), '%Y:%m:%d:%H:%M'))
                data = data.split(':')
                print('time: ' + data[2] + '.' + data[1] + '.' + data[0] + ' ' + data[3] + ':' + data[4])
                print('-' * 30)
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
                if id != '2000000007' and id != '2000000006':
                    if event.obj.peer_id != event.obj.from_id:
                        # Счетчик сообщений
                        with conn.cursor() as cursor:
                            cursor.execute("SELECT * FROM `users` WHERE `uid` ='" + from_id + "'")
                            rows = cursor.fetchall()
                            if cursor.rowcount == 0:
                                cursor.execute("INSERT INTO `users` (`uid`, `msg_week`, `msg_all`, `data`) VALUES('" + from_id + "', '1', '1', '" + dataplus + "')")
                            else:
                                data_now = data = str(datetime.strftime(datetime.now(), '%Y:%m:%d'))
                                lastmsg = data_now.split(':')
                                date1_str = str(lastmsg[2]) + '.' + str(lastmsg[1]) + '.' + str(lastmsg[0])
                                workdate = datetime.strptime(date1_str, "%d.%m.%Y")
                                str_day = str(calendar.day_abbr[workdate.date().weekday()]).lower()
                                row = d_user(from_id)
                                if row['msg_week'] == 700 and row['rang'] == 1:
                                    cursor.execute("UPDATE `users` SET `rang` = '2' WHERE (`id` = '" + from_id + "')")
                                if row['msg_week'] == 1500 and row['rang'] == 2:
                                    cursor.execute("UPDATE `users` SET `rang` = '3' WHERE (`id` = '" + from_id + "')")

                                if str_day.lower() == 'mon' and response == '!update':
                                    cursor.execute("SELECT * FROM `users`")
                                    rows = cursor.fetchall()
                                    rows_c = cursor.rowcount
                                    i = 0
                                    while i < rows_c:
                                        id_user = rows[i][0]
                                        all_msg = rows[i][6] + 1
                                        cursor.execute("UPDATE `users` SET `msg_week` = '0', `msg_all` = '" + str(all_msg) + "' WHERE (`id` = '" + str(id_user) + "')")
                                        i += 1
                                else:
                                    msg_count = rows[0][5] + 1
                                    msg_all = rows[0][6] + 1
                                    cursor.execute("UPDATE `users` SET `msg_week` = '" + str(msg_count) + "', `msg_all` = '" + str(msg_all) + "', `data` = '" + dataplus +"' WHERE (`uid` = '" + from_id + "')")
                        # Для сообщенией из беседы
                        if response == '!команды': send_message(id, message=commands)
                        elif response == '!admin': send_message(id, message=commands_admins)
                        elif response == '!правила': send_message(id, message=rules)
                        elif response == '!аниме': random_anime()
                        elif response == '!аниму': random_animu()
                        elif response == '!манхва': send_message(id, message='Ссылка на манхву: ' + link)
                        elif response == '!ранобэ': send_message(id, message='Ссылка на ранобэ: ' + linkr)
                        elif response == '!монетка': coin()
                        elif response == '!последняя глава': send_message(id, message='Ссылка на последнюю главу: ' + last_chapter)
                        elif response == '!ассоциация':
                            msg_chat = str(event.obj.conversation_message_id)
                            with conn.cursor() as cursor:
                                cursor.execute("SELECT SUM(shadows) FROM `users`")
                                rows = cursor.fetchall()
                            all_shad = str(rows[0][0])
                            send_message(id, message='Сообщений всего: ' + msg_chat + '\nТеней всего: ' + all_shad)
                        elif '!fight' in response or '!бой' in response:
                            reply = str(event.obj.fwd_messages[0]["from_id"])
                            if reply != from_id:
                                data = d_user(from_id)
                                data2 = d_user(reply)
                                if data['fight'] != 'none':
                                    send_message(id, message='У вас есть не отвеченный вызов')
                                elif data['shadows'] == 0:
                                    send_message(id, message='У вас нет теней')
                                elif data2['fight'] != 'none':
                                    send_message(id, message='Противнику уже бросили вызов')
                                elif data2['shadows'] == 0:
                                    send_message(id, message='У противника нет теней')
                                else:
                                    update_db('users', 'fight', from_id, reply)
                                    send_message(id, message='[id' + from_id + '|Вы] предложили [id' + reply + '|охотнику] бой')
                            else:
                                send_message(id, message='Вы не можете бросить самому себе вызов!')
                        elif '!разыграть' in response:
                            access_key = access()
                            if access_key >= 2:
                                num = response[11:len(response)]
                                prize(num)
                        elif '!украсть' in response:
                            access_key = access()
                            if access_key >= 4:
                                steal()
                        elif '!кости' in response:
                            num = ''
                            if len(response) > 6:
                                num = response[7:8]
                            bones(num)
                        elif '!преды' in response:
                            if str(event.obj.fwd_messages) != '[]':
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                data = d_user(reply)
                                send_message(id, message='Предупреждений: ' + str(data['complain']) + '/3')
                            else:
                                data = d_user(from_id)
                                send_message(id, message='Предупреждений: ' + str(data['complain']) + '/3')
                        elif '!босс' == response:
                            send_message(id, message='Босс вернулся в небытие')
                            # boss()
                        elif response == '!отклонить':
                            data = d_user(from_id)
                            update_db('users', 'fight', 'none', from_id)
                            send_message(id, message='Вы отклонили вызов')
                        elif response == '!принять': accept()
                        elif '!пред' in response:
                            access_key = access()
                            if access_key >= 2:
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                complains(reply)
                        elif '!бан' in response:
                            reply = str(event.obj.fwd_messages[0]["from_id"])
                            send_message(id, message='[id' + reply + '|Вы] забанены')
                        elif '!ник' in response: nickname()
                        elif response == '!стата' or response == '!статус':
                            if str(event.obj.fwd_messages) != '[]':
                                access_key = access()
                                if access_key >= 1:
                                    reply = str(event.obj.fwd_messages[0]["from_id"])
                                    status(reply)
                                else:
                                    send_message(id, message='У вас низкий ранг для этой команды')
                            else:
                                status(from_id)
                        elif response == '!топ':
                            access_key = access()
                            if access_key >= 1:
                                top_shadows()
                            else:
                                send_message(id, message='У вас нет прав для этой команды')
                        elif response == '!tmsg':
                            access_key = access()
                            if access_key >= 1:
                                top_msg()
                            else:
                                send_message(id, message='У вас нет прав для этой команды')
                        elif '!дать тени' in response: give_shadows()
                        elif '!повысить' in response:
                            access_key = access()
                            if access_key >= 2:
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                lvl_up(from_id, reply)
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')
                        elif '!наградить' in response:
                            access_key = access()
                            if access_key >= 2:
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                set_achievement(reply)
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')
                        elif '!снять пред' == response:
                            if str(event.obj.fwd_messages) != '[]':
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                data = d_user(reply)
                                complain = int(data['complain'])
                                complain -= 1
                                update_db('users', 'complain', str(complain), reply)
                                send_message(id, message='Предупреждение снято!')
                            else:
                                send_message(id, message='Вы никого не выбрали')
                        elif '!снять награду' in response:
                            access_key = access()
                            if access_key >= 2:
                                if str(event.obj.fwd_messages) != '[]':
                                    user = str(event.obj.fwd_messages[0]["from_id"])
                                    achievement = response[15:len(response)]
                                    del_achievement(user, achievement)
                                else:
                                    send_message(id, message='Вы не выбрали цель')
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')
                        elif '!stat' == response:
                            access_key = access()
                            if access_key >= 1:
                                stats_message()
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')

                    # Команды для ЛС бота
                    if event.obj.peer_id == event.obj.from_id:
                        if response == '!команды' or response == 'команды': send_message(id, message=commands_ls)
                        elif '!ник' in response: nickname()
                        elif '!стата' in response or 'стата' in response: status(from_id)
                        elif '!монетка' in response or 'монетка' in response: coin()
                        elif '!правила' in response or 'правила' in response: send_message(id, message=rules)
                        elif '!восстань' in response or 'восстань' in response: arise()
                        elif '!кости' in response or 'кости' in response:
                            num = ''
                            if len(response) > 6:
                                num = response[7:8]
                            bones(num)
                        elif '!аниме' in response or 'аниме' in response: random_anime()
                        elif '!аниму' in response or 'аниму' in response: random_animu()
                        elif '!преды' in response or 'преды' in response:
                            if str(event.obj.fwd_messages) != '[]':
                                reply = str(event.obj.fwd_messages[0]["from_id"])
                                data = d_user(reply)
                                send_message(id, message='Предупреждений: ' + str(data['complain']) + '/3')
                            else:
                                data = d_user(from_id)
                                send_message(id, message='Предупреждений: ' + str(data['complain']) + '/3')
                        elif '!босс' in response or 'босс' in response:
                            send_message(id, message='Босс вернулся в небытие')
                            # boss()
                        elif '!tshad' in response or 'tshad' in response: top_shadows()
                        elif '!tmsg' in response or 'tmsg' in response: top_msg()
                        elif '!сезон' in response or 'сезон' in response: anime_season()
                        elif '!топ аниме' in response or 'топ аниме' in response: top100anime()
                        elif '!топ манги' in response or 'топ манги' in response: top100manga()
                        elif '!скрыться' in response or 'скрыться' in response:
                            data = d_user(from_id)
                            if data['invis'] == 0:
                                update_db('users', 'invisible', '1', from_id)
                                send_message(id, message='Статистика скрыта')
                            elif data['invis'] == 1:
                                send_message(id, message='Вы уже скрыли свою статистику')
                        elif '!открыть' == response:
                            data = d_user(from_id)
                            if data['invis'] == 1:
                                update_db('users', 'invisible', '0', from_id)
                                send_message(id, message='Статистика открыта')
                            elif data['invis'] == 0:
                                send_message(id, message='Вы уже открыли свою статистику')
                        elif '!последняя глава' in response or 'последняя глава' in response: send_message(id, message='Ссылка на последнюю главу: ' + last_chapter)
                        elif '!манхва' in response or 'манхва' in response: send_message(id, message='Ссылка на манхву: ' + link)
                        elif '!ранобэ' in response or 'ранобэ' in response: send_message(id, message='Ссылка на ранобэ: ' + linkr)
                        elif '!важно' in response:
                            if id == '370633116' or id == '195365002':
                                warning = response[6:len(response)]
                                send_message(2000000004, 'Важная информация:\n' + warning.capitalize())
                                send_message(id, message='Информация отправлена')
                            else: send_message(id, message='У вас нет доступа к этой команде!')
                        elif '!link edit' in response:
                            if id == '370633116' or id == '195365002':
                                relink = response[11:len(response)]
                                setting[0] = relink
                                with open(r'settings.txt', 'w') as f:
                                    for line in setting:
                                        f.write(line + '\n')
                                    send_message(id, message='Ссылка на манхву изменена')
                            else: send_message(id, message='У вас нет прав для этой команды!')
                        elif '!chapter edit' in response:
                            if id == '370633116' or id == '195365002':
                                rechapter = response[14:len(response)]
                                setting[1] = rechapter
                                with open(r'settings.txt', 'w') as f:
                                    for line in setting:
                                        f.write(line + '\n')
                                    send_message(id, message='Ссылка на последнюю главу изменена')
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')
                        elif '!update' == response:
                            if id == '370633116' or id == '195365002':
                                with conn.cursor() as cursor:
                                    cursor.execute("SELECT * FROM `users`")
                                    rows = cursor.fetchall()
                                    rows_c = cursor.rowcount
                                i = 0
                                while i < rows_c:
                                    id_user = rows[i][0]
                                    rang = rows[i][3]
                                    with conn.cursor() as cursor:
                                        if rang == 0:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '10' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 1:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '1' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 2:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '2' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 3:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '3' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 4:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '4' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 5:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '5' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 6:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '6' WHERE (`id` = '" + str(id_user) + "')")
                                        elif rang == 7:
                                            cursor.execute(
                                            "UPDATE `users` SET `try` = '7' WHERE (`id` = '" + str(id_user) + "')")
                                    i += 1
                                send_message(2000000004, message='Количество попыток обновлено')
                                send_message(id, message='Кол-во попыток обновлено')
                            else:
                                send_message(id, message='У вас нет прав для этой команды!')
                        else:
                            send_message(id, message='Введите пожалуйста команду, если вы не знаете команд, '
                                                     'то наберите - !команды')
                # Приветствие пользователя когда он вступил в беседу
                if event.obj.action["type"] == 'chat_invite_user' and event.obj.peer_id != '2000000007' and event.obj.peer_id != '2000000006':
                    fullname = '[id' + str(event.obj.action["member_id"]) + '|охотник]'
                    with conn.cursor() as cursor:
                        cursor.execute("INSERT INTO `users` (`uid`, `msg_week`, `msg_all`, `data`) VALUES('" + str(event.obj.action["member_id"]) + "', '1', '1', '" + dataplus + "')")
                    send_message(id, message='Добро пожаловать ' + fullname + ' \n Для ознакомления с правилами напишите - !правила ')
                if event.obj.action["type"] == 'chat_kick_user' and event.obj.peer_id != '2000000007' and event.obj.peer_id != '2000000006':
                    fullname = '[id' + str(event.obj.action["member_id"]) + '|Охотник]'
                    with conn.cursor() as cursor:
                        cursor.execute("DELETE FROM `users` WHERE (`uid` = '" + str(event.obj.action["member_id"]) + "')")
                    send_message(id, message=fullname + ' пал в подземелье')
    except:
        continue
# 851 liens code
# 967 lines code 8:00 20.06.2020
# 895 lines code 19:00 20.06.2020