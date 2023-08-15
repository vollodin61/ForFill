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


# не понятно нужно ли это вообще
# @dataclass
# class UserBotConfig:
#     name: str
#     api_id: str
#     api_hash: str


@dataclass
class OtherParams:
    other_params: str
    my_id = '590018906'
    text_for_survey = 'Текст сообщения для тех, кто прошёл опрос'  # todo написать текст для тех, кто прошёл опрос
    tilda_chatbot_id = '265299531'


@dataclass
class UserBbot:
    env = Env()
    env.read_env()
    my_acc = Client(name="my_acc", api_id=env("_id_"), api_hash="_hash_", parse_mode=ParseMode.HTML)



# @dataclass  Возможно когда-то понадобится
# class UserBotConfig:
#     my_acc: UserBotConfig

@dataclass
class Config:
    bot: TgBotConfig
    db: DataBaseConfig
    other_p: OtherParams
    ubot: UserBbot
