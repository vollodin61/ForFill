import asyncio

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from autoanswer_bot.data.echo_bot_config import UserBbot, OtherParams
from autoanswer_bot.filters.custom_filters import pattern_for_tilda_request as patt, request_filter
from autoanswer_bot.utils.finder_pattern import patterns_finder



ubot = UserBbot.my_acc
my_id = OtherParams.my_id
text_for_survey = OtherParams.text_for_survey


# ms = ubot.send_message('me', f'user_id = {message.sender_chat}') вот это вот работает для каналов


@ubot.on_message()
def from_tilda(client: Client, message: Message):  # почему-то эта шляпа у меня только так работает,
    if message.from_user.id == 265299531:  # не смог сделать фильтр кастомный
        tg_nik = patterns_finder(pattern=patt, text=message.text)[0][9:]
        print('нашлося, работает фильтрик')
        ubot.send_message(tg_nik, text=f"{text_for_survey}, ник чувачка {tg_nik}")

    # todo вот тут должно быть добавление в базу в гугл-таблице


""" регистрация нового хендлера
my_acc.add_handler(MessageHandler(from_tilda, filters=filters.chat(chats=tilda_id)))"""

ubot.run()
