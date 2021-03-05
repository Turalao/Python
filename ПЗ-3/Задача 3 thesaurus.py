dict_names = {}

def thesaurus (*args):
    """ ищет совпадения по ключу, иначе создает новую пару ключ - значение"""
    for item in args:
        if dict_names.get(item[0], None) != None:
            n = dict_names[item[0]]
            n.append(item)
            dict_names[item[0]] = n
        else:
            dict_names.setdefault(item[0], [item])
    print(dict_names)

thesaurus("Иван", "Мария", "Петр", "Илья")