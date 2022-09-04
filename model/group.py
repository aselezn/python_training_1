
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):  # None - дает возможность не инициализировать поля
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


#метод для репрезинтации атрибутов
    def __repr__(self):
        return '%s:%s' % (self.id, self.name)


#для сравнение атрибутов логически, а не физически (до этой функции система сравнивала объекты по местонахождению в памяти)
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name