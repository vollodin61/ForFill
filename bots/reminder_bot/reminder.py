from pyrogram import Client
from pyrogram.types import Message
from time import sleep
from datetime import datetime
from dotenv import find_dotenv, load_dotenv
import os

# 35642115,
_id_ = os.getenv('_id_')
_hash_ = os.getenv('_hash_')

if not find_dotenv():
    exit('Не удалось найти файл .env')
else:
    load_dotenv()

id_list = [
    1964621172
]


def reminds():
    count = 0
    now_moment = datetime.now().strftime("%Y:%b:%d %H:%M:%S")
    while count < 57:
        for i in id_list:
            try:
                with Client('my_account', _id_, _hash_) as app:
                    app.send_message(i, 'Время для быстрого и легкого комплимента!')
            except:
                with Client('my_account', _id_, _hash_) as app:
                    app.send_message('me', f'{i} не получил сообщение похвалить себя')
                with open('log.txt', 'a+', encoding='utf-8') as f:
                    f.write(f'\n{i} не получил сообщение в {now_moment}')

        print(f'Цикл №{count + 1} завершен')
        sleep(600)
        count += 1


def sender_hashtags():
    id = 979328150
    try:
        with Client('my_account', _id_, _hash_) as app:
            app.send_message(id, '#позитивныедумы')
    except:
        app.send_message('me', f'Бот Геннадий не получил сообщение')


sender_hashtags()