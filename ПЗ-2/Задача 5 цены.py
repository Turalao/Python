start_values = [10.50, 5.5, 7.07, 6, 100, 0.9, 123.98, 55.45, 14.3, 3.7]
first_price = []
print(id(start_values))
i: int = 0
while i < len(start_values):
    first_price.append(f'{str(int(start_values[i]//1)).zfill(2)} руб {str(int(start_values[i]%1*100)).zfill(2)} коп')
    i = i+1
print(f' цены: {", ".join(first_price)}')
print(f' id начального списка {id(start_values)}')
start_values.sort()
i = 0
while i < len(start_values):
    start_values[i] = f'{str(int(start_values[i]//1)).zfill(2)} руб {str(int(start_values[i]%1*100)).zfill(2)} коп'
    i += 1
print(f' цены по возрастанию: {", ".join(start_values)} ')
print(f' id начального списка {id(start_values)}')
from copy import deepcopy
lower_price = deepcopy(reversed(start_values))
print(f' цены по убыванию: {", ".join(lower_price)}')
print(f'самые большие цены: {", ".join(start_values[-5:])}!')