import json
import requests

from .models import Character

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

def search_character(name:str, server=None):
    name = url_string(name)
    search_url = xivapi_url + f"character/search?name={name}"
    if server: search_url += f"&server={server}"

    print(search_url)

    response = json.loads(requests.get(search_url).content)
    results = response["Results"]

    return results

def get_character(id:int) -> Character:
    profile_url = xivapi_url + f'character/{str(id)}'
    response = json.loads(requests.get(profile_url).content)
    
    character = response['Character']
    name = character['Name']
    portrait = character['Portrait']
    jobs = character['ClassJobs']

    character = Character(id, name, jobs, portrait)

    return character



def url_string(string:str):
    return string.replace(" ", "+")