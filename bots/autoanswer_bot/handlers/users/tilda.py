from pyrogram.types import Message
from autoanswer_bot.just_go import my_acc


def autoanswer(message: Message):
    chat_id = '590018906'
    text = message.text
    my_acc.send_message(chat_id=chat_id, text='text')
