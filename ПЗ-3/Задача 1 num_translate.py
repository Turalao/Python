

def num_translate(s1):
    """выводит перевод цифр с английского на русский в нижнем регистре"""
    dict_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': "девять", 'ten': 'десять'}
    print(f'перевод: {dict_translate.get(s1, "неверно введено")}')


num_translate(input('введите число на английском '))
