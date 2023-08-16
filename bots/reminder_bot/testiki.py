from pyrogram import Client
from time import sleep
from pyrogram.raw.functions.users.get_full_user import GetFullUser
from datetime import datetime
id = '26315421'
hash = '6381a688ef53e5f6dfc29bbc29bc9381'
id_list = ['null', 'dfdf',]
count = 0

#
# while count < 2:
#     for i in id_list:
#         try:
#             with Client('my_account', id, hash) as app:
#                 app.send_message(i, 'Самое время похвалить себя!\nИ сделать пару "щелчков"!))')
#         except:
#             with Client('my_account', id, hash) as app:
#                 app.send_message('me', f'{i} не получил сообщение')
#     count += 1

dt = datetime.now()
time = dt.time()
time.strftime('%H:%M:%S')

print('dfdfdf')