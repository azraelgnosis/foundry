class Character:
    __slots__ = ['name', 'player', 'bio', "characteristics", 'attributes', 'occupation']

    def __init__(self):
        
        self.characteristics = {
            "STR": 0,
            "CON": 0,
            "POW": 0,
            "DEX": 0,
            "APP": 0,
            "SIZ": 0,
            "INT": 0,
            "EDU": 0
        }

        self.attributes = {
            "Luck": 0,
            "MP": 0,
            "DMG": 0,
            "Build": 0,
            "HP": 0,
            "SAN": 0,
            "CR": 0
        }
        self.bio = {
            'age': 0,
            'gender': 0,
            'residence': "",
            'birthplace': ""
        }

    def _set_build(self):
        pass