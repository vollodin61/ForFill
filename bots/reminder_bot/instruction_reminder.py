from pyrogram import Client
from time import sleep
from datetime import datetime

"""Этот скрпит от твоего имени в Телеграм может отправлять сообщения"""

_id_ = 'здесь твой id'
_hash_ = 'здесь твой токен'
#  Вот тут https://mob25.com/client-api-v-telegram/ инструкция, откуда их взять

id_list = []  # Здесь через запятую список id аккаунтов, которым будешь рассылать
                # Чтобы сообщения отправлялись, нужно добавить всех адресатов к себе в контакты в телеге

count = 0  # Счётчик циклов рассылки

log_time = datetime.now().time().strftime('%H:%M:%S')  # Это время "сейчас", если оно надо (мне было надо)

while count < 10:  # Это цикл, который будет повторяться пока переменная count меньше 10
    for i in id_list:  # Это цикл, который перебирает все id из списка id_list
        try:  # Здесь пытается
            with Client('my_account', _id_, _hash_) as app:  # Тут происходит логин в телеге от твоего имени
                app.send_message(i, 'Самое время похвалить себя!\nИ сделать пару "щелчков"!)')  # Тут
                            # по очередному id списка id_list отправляется сообщение, и выход из аккаунта (магия with)

        except:  # Если не получилось в try, то делаем следующее (опционально, мне вот такое надо было)
            with Client('my_account', _id_, _hash_) as app:  # Опять логин в телеге от твоего имени
                app.send_message('me', f'{i} не получил сообщение похвалить себя')  # Тут я сам себе отправлял сообщение
                                # с id аккаунта, которому не получилось отправить (и опять магия with)

            with open('log.txt', 'a+', encoding='utf-8') as f:  # Тут в свежесозданный файл записывается (дописывается)
                f.write(f'\n{i} не получил сообщение в {log_time}')  # id аккаунта, которому не отправилось,
                                        # и время во сколько это случилось (и закрывается текстовый файл, магия with)

    print(f'Цикл №{count + 1} завершен')  # Тут просто в консоль выводится сообщение для меня,
                                    # что очередной цикл завершен
    sleep(3600)  # тут просто выжидается 3600 секунд (мне нужно было раз в час отправлять сообщения)
    count += 1  # тут переменная count увеличивается на 1 (это для 13й строки надо), и цикл уходит на следующий круг