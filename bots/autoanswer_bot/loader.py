from pyrogram import Client
import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    print("not find dotenv, break")
    load_dotenv()

_id_ = os.getenv('_id_')
_hash_ = os.getenv('_hash_')

my_acc = Client("my_acc", _id_, _hash_)


async def main():
    my_acc.run()


if __name__ == '__main__':
    main()
