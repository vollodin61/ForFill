import asyncio

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from autoanswer_bot.data.echo_bot_config import UserBbot, OtherParams

my_id = OtherParams.my_id

tilda_id = OtherParams.tilda_chatbot_id
ubot = UserBbot.my_acc


@ubot.on_message()
def from_tilda(client: Client, message: Message):
    # if message.from_user.id == tilda_id:
    #     message.copy(590018906)

    # i = message.chat.id
    # k = message.forward_from.id
    # if i == -1001930780123:
    # if k == 265299531:
    # ubot.send_message(590018906, text=f'chat_id = {i}')
    # ms = ubot.send_message('me', f'user_id = {message.sender_chat}') вот это вот работает для каналов
    please = message.from_user.id
    if please == 265299531:
        message.forward('me')
        fu = ubot.send_message('me',
                               f'us_id = {message.from_user.id}')  # вот эта хуйня пересылает юзер_ай_ди, осталось фильтр придумать, чтобы работал
        print("УРААААА!!!")
        print(type(fu))


# my_acc.add_handler(MessageHandler(from_tilda, filters=filters.chat(chats=tilda_id)))

ubot.run()
