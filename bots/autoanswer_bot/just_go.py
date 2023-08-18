from pyrogram import Client
from pyrogram.types import Message

from autoanswer_bot.data.echo_bot_config import UserBbot, OtherParams
from autoanswer_bot.filters.custom_filters import pattern_for_tilda_request as patt
from autoanswer_bot.utils.finder_pattern import patterns_finder

ubot = UserBbot.my_acc
my_id = OtherParams.my_id
text_for_survey = OtherParams.text_for_survey


@ubot.on_message()
def from_tilda(client: Client, message: Message):
    if message.from_user.id == 265299531:
        tg_nik = patterns_finder(pattern=patt, string=message.text)
        print(tg_nik)
        print('нашлося, работает фильтрик')
        ubot.send_message(tg_nik, text=f"{text_for_survey}")


ubot.run()
