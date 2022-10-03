import json

from model.group import Group
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #в переменной будут буквы + символы + пунктуация + 10 раз повторяем пробел
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генерируется случайная длина строки не превышающая максимальную


testdata = [Group(name="", header="", footer="")] + [
        Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
        for i in range(n) #5 раз создаем группы с рандомными данными
]

#путь к файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


#конфигурация данных и преобразование в json
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2) #indent - формотирует данные красиво
    out.write(jsonpickle.encode(testdata))