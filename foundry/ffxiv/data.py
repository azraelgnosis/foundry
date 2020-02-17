import json
import os
import requests

from .models import Character

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