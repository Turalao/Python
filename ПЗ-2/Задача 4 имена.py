start_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
while i<4:
    print(f'Добрый день, {(start_list[i].rsplit()[-1]).capitalize()}!')
    i = i+1