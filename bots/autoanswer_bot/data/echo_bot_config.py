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
    my_id = '590018906'
    text_for_survey = ('Текст сообщения для тех, который мы ещё не придумали.\n'
                       'Спасибо, что прошли опрос))')
    tilda_chatbot_id = '265299531'


@dataclass
class UserBbot:
    env = Env()
    env.read_env()
    my_acc = Client(name="my_acc", api_id=env("_id_"), api_hash="_hash_", parse_mode=ParseMode.HTML)


@dataclass
class Config:
    bot: TgBotConfig
    db: DataBaseConfig
    other_p: OtherParams
    ubot: UserBbot
