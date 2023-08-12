from autoanswer_bot.loader import my_acc
from pyrogram.types import Message, Chat
# from pyrogram.handlers import message_handler

@my_acc.on_message()
async def autoanswer(message: Message):
    pass # TODO при помощи фильтра, который импортируем из .filters, отправляем ссылку-приглос
