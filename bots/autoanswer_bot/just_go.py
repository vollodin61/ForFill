from pyrogram import Client
from pyrogram.types import Message
from data.echo_bot_config import UserBot, OtherParams
from utils.finder_pattern import survey_patterns_finder, order_patterns_finder

ubot = UserBot.my_acc
my_id = OtherParams.my_id
tilda_chatbot_id = OtherParams.tilda_chatbot_id
test_chat_id = OtherParams.test_chat_id
text_if_survey = OtherParams.texts_for_ans_bot['if_survey']
text_if_club = OtherParams.texts_for_ans_bot['if_club']
text_if_course = OtherParams.texts_for_ans_bot['if_course']
dt_now = OtherParams.dt_now


@ubot.on_message()
def from_tilda(client: Client, message: Message):
    try:
        if message.from_user.id == tilda_chatbot_id:

            if OtherParams.webinar in message.text:
                print(f'!!! {message.chat.id} - это чат id')
                tg_nik = order_patterns_finder(string=message.text)
                print(tg_nik)
                ubot.send_message(chat_id=tg_nik, text=f"{OtherParams.texts_for_ans_bot['if_survey']}")
            if OtherParams.club in message.text:
                tg_nik = order_patterns_finder(string=message.text)
                ubot.send_message(chat_id=tg_nik, text=f"{OtherParams.texts_for_ans_bot['if_club']}")
            if OtherParams.course in message.text:
                tg_nik = order_patterns_finder(string=message.text)
                ubot.send_message(chat_id=tg_nik, text=f"{OtherParams.texts_for_ans_bot['if_course']}")
            else:
                tg_nik = survey_patterns_finder(string=message.text)
                ubot.send_message(chat_id=tg_nik, text=f"{text_if_survey}")

    except Exception as err:
        err_text = f'\n{dt_now} - Что-то пошло не так {err}'
        print(err_text)
        ubot.send_message(chat_id=my_id, text=err_text)


ubot.run()
