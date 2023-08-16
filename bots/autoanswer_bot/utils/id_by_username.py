from pyrogram import filters
from pyrogram.types import Message, Chat

from autoanswer_bot.just_go import ubot


def username_to_id(text):
    pattern = None
    chat_id = None
    # Todo тут мы ищем паттерн, и потом обрезаем паттерн до username
    # todo потом по username при помощи Chat ищем chat_id, или my_acc.get_chat("username") вот так

    return chat_id
