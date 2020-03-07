from .data import RACES

class Model:
    __slots__ = ["name"]

    def __init__(self, name=None):
        self.name = name
    
    def json(self):
        return {key: getattr(self, key) for key in self.__slots__}

    @staticmethod
    def from_json(json:dict): ...

    def __repr__(self): return f"{self.name}"

#! need to account for multiclassing
class Character(Model):
    __slots__ = ["race", "level", "class"]

    def __init__(self): ...
    
    @staticmethod
    def from_json(json:dict):
        new_character = Character()
        for key, val in json.items():
            setattr(new_character, key, val)
        return new_character

    def __repr__(self): return f"{self.name}"

class Spell(Model):
    __slots__ = ["level", "classes", "school", "cast_time", "range", "duration", "components", "duration"]    

    @staticmethod
    def from_json(json:dict):
        new_spell = Spell
        for key, val in json.items():
            setattr(new_spell, key, val)