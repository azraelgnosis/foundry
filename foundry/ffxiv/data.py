import json
import os
import requests

from .models import Character, Quest

data_path = os.path.join(os.path.dirname(__file__), 'data')

xivapi_url = 'https://xivapi.com/'

WORLDS = {
    "North American": {
        "Aether": {},
        "Crystal": {},
        "Primal": [
            "Behemoth",
            "Leviathan"
        ]
    }
}

#! Should probably go somewhere in models
ELEMENTS = ("Earth", "Fire", "Ice", "Lightning", "Water", "Wind")
CRYSTAL_CONFIGURATIONS = ("Shard", "Crystal", "Cluster") #? There's probably a better word than "configuraiton"
CRYSTALS = {element: [configuration for configuration in CRYSTAL_CONFIGURATIONS] for element in ELEMENTS}

VALUES = ("Unsellable",)

#TODO: Add separate pages
def search_character(name:str, server=None):
    name = url_string(name)
    search_url = xivapi_url + f"character/search?name={name}"
    if server: search_url += f"&server={server}"

    print(search_url)

    results = []
    response = json.loads(requests.get(search_url).content)
    num_results = response['Pagination']['ResultsTotal']
    results_per_page = 50 # built-in to Lodestone's api
    num_pages = (num_results // results_per_page) + 1
    
    for page in range(1, num_pages+1):
        search_url_by_page = f"{search_url}&page={page}"
        response = json.loads(requests.get(search_url_by_page).content)
        results.extend(response["Results"])
        for result in response['Results']:
            character = Character().f

    return results

def get_character_api(lodestone_id:int) -> Character:
    profile_url = xivapi_url + f'character/{str(lodestone_id)}'
    response = json.loads(requests.get(profile_url).content)
    
    character = response['Character']
    name = character['Name']
    portrait = character['Portrait']
    jobs = character['ClassJobs']

    character = Character(lodestone_id, name, jobs, portrait)

    return character

def load_characters() -> list:
    pass

def get_character_db(lodestone_id:int) -> Character:
    pass

def url_string(string:str):
    return string.replace(" ", "+")

def get_data(data_type:str) -> dict:
    from. models import Action, Item, Location, Quest

    types = {
        "actions": Action,
        "items": Item,
        "locations": Location.from_json,
        "quests": Quest
    }
    
    with open(f"{data_path}/{data_type}.json", "r") as f:
        json_data = json.load(f)

    # data = {key: types.get(data_type)(obj) for key, obj in json_data.items()}
    data = {}
    for key, obj in json_data.items():
        data[key] = types.get(data_type)(obj)

    return data

def get_items() -> dict:
    from .models import Item

    with open(f"{data_path}/items.json", "r") as f:
        json_data = json.load(f)

    items = {name: Item(obj) for name, obj in json_data.items()}

    return items

def set_data(data_type:str, data:dict):
    json_data = {name: obj.json() for name, obj in data.items()}

    with open(f"{data_path}/{data_type}.json", "w") as f:
        json.dump(json_data, f, indent=4)