import json
import os

path = os.path.dirname(__file__)

anyflip_books = {
    "master": "ncyu",
    "monster": "riec",
    "player": "nkyr"
}

RACES = {
    "Gnome": {
        "Rock": "Rock Gnome",
        "Forest": "Forest Gnome"
    }
}

MAGIC_SCHOOLS = ("Conjuration", "Divination", "Evocation")

def get_spells():
    with open(f'{path}/data/spells.json', 'r') as f:
        spells = json.load(f)

    return spells