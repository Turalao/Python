nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []


def get_jokes(n):
    """рандомно склеивает 3 слова из списков и добавляет в список"""
    from random import choice
    for i in range(n):
        jokes.append((' ').join([choice(nouns),choice(adverbs),choice(adjectives)]))
    print (jokes)


get_jokes(5)
