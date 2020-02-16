class Character:
    __slots__ = ["player", "name", "race", "clan", "jobs", "server", 'portrait']

    def __init__(self, id, name, jobs={}, portrait=None):
        self.name = name
        self.jobs = jobs
        self.portrait = portrait

    def json(self):
        json = {
            'name': self.name,
            'jobs': {
                "Hand": {},
                "Land": {},
                "Magic": {
                    "Astrologian": {},
                    "Black Mage": {},
                    "Blue": {},
                    "Red Mage": {},
                    "Scholar": {},
                    "Summoner": {},
                    "White Mage": {}
                },
                "War": {
                    "Bard": {},
                    "Dancer": {},
                    "Dark Knight": {},
                    "Dragoon": {},
                    "Gunbreaker": {},
                    "Machinist": {},
                    "Monk": {},
                    "Ninja": {},
                    "Paladin": {},
                    "Samurai": {},
                    "Warrior": {}
                }
            }
        }



        return json

class Job:
    DISCIPLINES = {
        "Combat": ["War", "Magic"],
        "Crafting": ["Hand", "Land"]
    }
    __slots__ = ["name", "discipline", "level", "log"]

    def __init__(self, name:str, discipline:str):
        self.name = name
        self.discipline