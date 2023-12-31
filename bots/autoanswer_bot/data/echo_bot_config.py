from _datetime import datetime

from pyrogram import Client
from dataclasses import dataclass
from environs import Env
from pyrogram.enums import ParseMode


@dataclass
class DataBaseConfig:
    host: str
    password: str
    login: str
    database: str


@dataclass
class TgBotConfig:
    token: str
    admins_ids: list[int]
    use_redis: bool = False


@dataclass
class OtherParams:
    other_params: str
    my_id = 590018906
    tilda_chatbot_id = 265299531
    test_chat_id = -1001930780123
    pyro_bot_errors_chat_id = -1001907788569

    dt_now = datetime.now().strftime("%H:%M:%S %Y-%m-%d")

    webinar = '700 RUB'
    club = '2000 RUB'
    course = '7000 RUB'
    course_again = '3500 RUB'

    texts_for_ans_bot = {
        'if_survey': ('Здравствуйте! Я Филатова Ирина, автор курса "Доброе слово для кошки"\n'
                      'Спасибо, что прошли опрос!)\n\n'
                      'Удалось ли прочитать рекомендации для себя? Что думаете, насколько узнали себя?)\n'
                      'Буду рада, если поделитесь впечатлением)'),
        'if_club': 'Привет! Добро пожаловать в клуб!\n\nПрисоединяйся!)\nhttps://t.me/+Yw9gMOk5i2E0YzMy ',
        'if_club_again': 'Привет! Спасибо за продление участия в Клубе!)'
                         '\n\nПрисоединяйся!)\nhttps://t.me/+Yw9gMOk5i2E0YzMy ',
        'if_course': 'Здравствуйте! Я Филатова Ирина, автор курса "Доброе слово для кошки"\n'
                     'Спасибо за проявленный интерес и доверие! Оплата прошла успешно.\n\n'
                     'Ссылку на чат я пришлю Вам за 2 дня до старта.\n\n'
                     'Иногда алгоритмы дают сбои. Если ссылка не пришла вовремя, то напишите мне',
        'if_course_again': 'Привет! \n'
                           'Спасибо за проявленный интерес и доверие! Добро пожаловать на повторное прохождение курса!\n'
                           'Ссылка на чат придёт сюда за 2 дня до старта.\n\n'
                           'Иногда алгоритмы телеграма дают сбои. Если ссылка не пришла вовремя, то напишите мне',
    }


@dataclass
class UserBot:
    env = Env()
    env.read_env()
    fill_acc = Client(name="fill_acc", api_id=env("ifill_id"), api_hash=env("ifill_hash"), parse_mode=ParseMode.HTML)
    my_acc = Client(name="my_acc", api_id=env("_id_"), api_hash=env("_hash_"), parse_mode=ParseMode.HTML)


@dataclass
class Config:
    bot: TgBotConfig
    db: DataBaseConfig
    other_p: OtherParams
    ubot: UserBot
