import json
import os

path = os.path.dirname(__file__)

def get_spells():
    with open(f'{path}/data/spells.json', 'r') as f:
        spells = json.load(f)

    return spells


anyflip_books = {
    "master": "ncyu",
    "monster": "riec",
    "player": "nkyr"
}