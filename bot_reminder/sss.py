from datetime import datetime

dt = datetime.now()
time = dt.time()
a = time.strftime('%H:%M:%S')

with open('d.txt', 'a+', encoding='utf-8') as f:
    f.write(f'\n{a}')