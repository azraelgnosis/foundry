

class Character:
    __slots__ = ['lodestone_id', "player", "name", "race", "clan", "jobs", "server", 'avatar', 'portrait']

    def __init__(self, lodestone_id=None, name=None, jobs={}, avatar=None, portrait=None, server=None):
        self.lodestone_id = lodestone_id
        self.name = name
        self.jobs = jobs
        self.portrait = portrait
        self.avatar = avatar
        self.server = server

    #     self._set_jobs()

    # def _set_jobs(self):
    #     for discipline, jobs in JOBS.items():
    #         for job in jobs:
    #             self.jobs[job] = Job(name=job, discipline=discipline)

    def json(self):
        json = {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
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
                    ("Lancer", "Dragoon"): {
                        "Log": []
                    },
                    "Gunbreaker": {},
                    "Machinist": {},
                    "Monk": {},
                    "Ninja": {},
                    "Paladin": {},
                    "Samurai": {},
                    "Warrior": {}
                }
            },
            'portrait': self.portrait,
            'avatar': self.avatar
        }

        return json

    def from_api(self, json_data:dict):
        Character = json_data['Character']
        Avatar = Character['Avatar']

class CharacterCreator:
    @staticmethod
    def from_xiv_api(json_data):
        Character = json_data['Character']
        Avatar = Character['Avatar']


class Job:
    JOBS = {
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
    DISCIPLINES = [disciple for disciple in JOBS.keys()]
    JOB_list = [(job for job in JOBS) for discipline, JOBS in JOBS.items()]

    __slots__ = ["name", "discipline", "level", "log", "quests"]

    def __init__(self, name:str, discipline:str):
        self.name = name if name in Job.JOB_list else KeyError
        self.discipline = discipline if discipline in Job.DISCIPLINES else KeyError

class Action:
    __slots__ = ["name", "type", "level", "description"]

class Spell(Action):
    __slots__ = ["job", "dmg", "effect", "mp_cost", "cast_time", "recast", "range", "radius", "target"]

class Ability(Action):
    __slots__ = ["effect"]

class Effect:
    __slots__ = ["target", "effect", "degree", "duraiton"]

class Recipe:
    TYPES = {
        "Alchemist": ["Reagent", "One-handed Conjurer's Arm", "Medicine", "Arcanist's Grimoire"],
        "Culinarian": ["Ingredient", "Meal", "Fishing Tackle", "Gardening", "Tabletop", "Miscellany", "Dye"],
        "Other": ["Other"]
    }
    __slots__ = ["name", "job", "level", "type", "num_crafted", "difficulty", "durability", "max_quality", "materials", "crystals"]

    def __init__(self, name, job, level, type, num_crafted, difficulty, durability, max_quality, materials, crystals):
        self.name = name
        self.job = job
        self.level = level
        self.type = type
        self.num_crafted = num_crafted
        self.difficulty = difficulty
        self.durability = durability
        self.max_quality = max_quality
        self.materials = materials
        self.crystals = crystals

    def json(self):
        json = {key: getattr(self, key) for key in self.__slots__}

        return json