from pyrogram import filters
from pyrogram.types import Message

from autoanswer_bot.data.echo_bot_config import OtherParams
from autoanswer_bot.utils.finder_pattern import patterns_finder

tilda_bot_id = OtherParams.tilda_chatbot_id
pattern_for_tilda_request = "Input_2: @\w+|Input_2: \w+"
pattern_for_tilda_order = r'Ссылка_на_Телеграм: \w+'


# todo здесь ещё может быть другие разные покупки, на них будут другие разные ответы
# todo может быть 
def request_filter(_, __, m: Message):
    return m.from_user.id == 265299531


request_flt = filters.create(request_filter)
