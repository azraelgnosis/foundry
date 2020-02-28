from .data import RACES

#! need to account for multiclassing
class Character:
    __slots__ = ["name", "race", "level", "class"]

    def __init__(self): ...

    def json(self): return {key: getattr(self, key) for key in self.__slots__}
    
    @staticmethod
    def from_json(json:dict): return Character()

    def __repr__(self): return f"{self.name}"

class Spell:
    __slots__ = ["name", "level", "classes", "school", "cast_time", "range", "duration", "components"]

    def json(self):
        return {key: getattr(self, key) for key in self.__slots__}

    def __repr__(self): return f"{self.name}"