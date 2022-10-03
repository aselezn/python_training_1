from model.group import Group
import random
import string


constant = [
    Group(name="name_1", header="header_1", footer="footer_1",
    Group(name="name_2", header="header_2", footer="footer_2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #в переменной будут буквы + символы + пунктуация + 10 раз повторяем пробел
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генерируется случайная длина строки не превышающая максимальную


testdata = [Group(name="", header="", footer="")] + [
        Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
        for i in range(5) #5 раз создаем группы с рандомными данными
]
