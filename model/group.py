
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):  # None - дает возможность не инициализировать поля
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id