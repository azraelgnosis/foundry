class Model:
    """
    Serves as the bases for all model classes
    """
    __slots__ = ["name"]
    def __init__(self, json:dict):
        for attr in self.__slots__: setattr(self, attr, None)
        for key, val in json.items(): setattr(self, key, val)

    @staticmethod
    def from_dict(mapping:dict) -> 'Model': ...
    
    def json(self): return {key: getattr(self, key) for key in self.__slots__}
    def __repr__(self): return f"{self.name}"

class Location(Model):
    TYPES = ["Landmass", "Region", "Zone", "Area"]

    __slots__ = ['name', 'type', 'subregions', 'within']

    def __init__(self, name=None, loc_type=None, within=[]):
        self.name = name
        self.type = loc_type
        self.within = within

        self.subregions = {}

    def _set_subregions(self):
        for key, subregion in self.subregions.items():
            self.subregions[key] = Location.from_dict(subregion)

    def get_subregion(self, subregion:str) -> 'Location':
        return self.subregions.get(subregion)

    def add_subregion(self, subregion:'Location'):
        self.subregions[subregion.name] = subregion
    
    def del_subregions(self, subregion:'str'):
        del self.subregions[subregion]

    @staticmethod
    def from_dict(JSON:dict) -> 'Location':
        new_location = Location()
        for key, val in JSON.items():
            setattr(new_location, key, val)

        new_location._set_subregions()

        return new_location

    def __repr__(self): return f"{self.name}: {self.type}"


class NPC(Model):
    __slots__ = ["name", "gender", "race", "subrace", "locations", "organization", "services", "bio", "quests_started", "quests_involved"]

class Character(Model):
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


class Job(Model):
    #! The jobs are dicts rather than strings
    #! How to handle role classificaitons?
    JOBS = {
        "Hand": {
            "Culinarian"
        },
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

class Log(Model):
    __slots__ = []

class Action(Model):
    __slots__ = ["name", "type", 'job', "level", "description"]

class Spell(Action):
    __slots__ = ["job", "dmg", "effect", "mp_cost", "cast_time", "recast", "range", "radius", "target"]

class Ability(Action):
    __slots__ = ["effect"]

class Effect(Model):
    __slots__ = ["attribute", "change", "duration"]

class Recipe(Model):
    #! duplicate of Material.TYPES?
    TYPES = {
        "Alchemist": ["Reagent", "One-handed Conjurer's Arm", "Medicine", "Arcanist's Grimoire"],
        "Culinarian": ["Ingredient", "Meal", "Fishing Tackle", "Gardening", "Tabletop", "Miscellany", "Dye"],
        "Other": ["Other"]
    }
    
    __slots__ = ["name", "level", "type", "num_crafted", "difficulty", "durability", "max_quality", "materials", "crystals"]

    def __init__(self, materials:dict={}, crystals:dict={}):
        self.materials = materials
        self.crystals = crystals
    # def __init__(self, name, level, type, num_crafted, difficulty, durability, max_quality):
    #     self.name = name
    #     self.level = level
    #     self.type = type
    #     self.num_crafted = num_crafted
    #     self.difficulty = difficulty
    #     self.durability = durability
    #     self.max_quality = max_quality

    def set_materials(self, materials:dict={}):
        for material, num in materials.items():
            if material:
                self.materials[material] = int(num)
        
    def set_crystals(self, crystals:dict=None):
        for crystal, num in crystals.items():
            if crystal:
                self.crystals[crystal] = int(num)

    @staticmethod
    def from_dict(mapping:dict) -> 'Recipe':
        new_recipe = Recipe()
        for attr in Recipe.__slots__:
            if mapping.get(attr):
                setattr(new_recipe, attr, mapping.get(attr))
        
        #? Any use to coercing any ints?
        materials = {mapping.get('material'+str(i)): mapping.get('num_materials'+str(i)) for i in range(1, 7)}
        new_recipe.set_materials(materials)

        crystals = {
            mapping.get('type_crystalsA'): mapping.get('num_crystalsA'),
            mapping.get('type_crystalsB'): mapping.get('num_crystalsB')
            }
        new_recipe.set_crystals(crystals)
        
        return new_recipe

class Item(Model):
    TYPES = ('Other', 'Ingredient', 'Meal', 'Weapon', 'Armor')

    #? obtained_by, purchased_from, dropped_by, used_for
    __slots__ = ["name", "type", "subtype", "sell_value", "description"]    

class Meal(Item):
    __slots__ = ["effects"]

class Gear(Item): # Weapons and Armor
    __slots__ = ["jobs", "level", "req_level", "bonuses", "materia_slots"]
class Weapon(Gear):
    WEAPON_TYPES = ('Grimoire')
    __slots__ = ["damage", "delay", "auto_attack"]

class Armor(Gear):
    ARMOR_TYPES = ('Body')
    __slots__ = ["defence", "mag_defence"]

class Quest(Model):
    __slots__ = ["name", "quest_giver", "location", "quest_line", "level", "exp", "gil", "previous", "next", "description", "steps", "journal"]

    def __repr__(self): return f"{self.name}"