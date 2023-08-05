txt = "text.txt"
lst = [
    '1️⃣', '1️⃣ ',
    '2️⃣', '2️⃣ ',
    '3️⃣', '3️⃣ ',
    '4️⃣', '4️⃣ ',
    '5️⃣', '5️⃣ ',
    '6️⃣', '6️⃣ ',
]
n_lst = set()
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
nums = '1234567890'

with open(txt, 'r', encoding='utf-8') as t1:
    a = t1.readlines()
    for i in a:
        for n in lst:
            if i.startswith(n):
                i = i.lstrip(n)
                i = i.rstrip('\n')
                if i.startswith(' '):
                    i = i.lstrip(' ')
                    n_lst.add(i)

                    with open('new_text.txt', 'w', encoding='utf-8') as new_file:
                        for _ in n_lst:
                            new_file.write(_ + '\n')