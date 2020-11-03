from lorekeeper import Model

class Item(Model):
    pass

class Weapon():  #! TODO
    __slots__ = ('name', 'type', 'strength' 'focus_attack')
    columns = ('name', 'type', 'strength' 'focus_attack')

class Equipment():
    pass