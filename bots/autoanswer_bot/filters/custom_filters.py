from pyrogram import filters
from pyrogram.types import Message

from data.echo_bot_config import OtherParams

tilda_bot_id = OtherParams.tilda_chatbot_id
pattern_for_tilda_request = r"Input_2: @\w+|Input_2: \w+"
pattern_for_tilda_order = r'Ссылка_на_Телеграм: \w+|Ссылка_на_Телеграм: @\w+'


def request_filter(_, __, m: Message):
    return m.from_user.id == 265299531


request_flt = filters.create(request_filter)
