from flask import (
    Blueprint, render_template, request
)
import json

from .data import (
    WORLDS, search_character, get_character_api, get_data, set_data
)
from .models import Character, Job, Item

bp = Blueprint('ffxiv', __name__, subdomain='ffxiv')

@bp.route('/', methods=('GET', 'POST'))
def index():
    characters = None

    if request.method == 'POST':
        name = request.form['name']
        server = request.form['server']

        characters = search_character(name, server)

    return render_template('ffxiv/index.html', worlds=WORLDS, characters=characters)

@bp.route('/characters/<int:lodestone_id>')
def character(lodestone_id):
    character = get_character_api(lodestone_id)

    return render_template('ffxiv/character.html', character=character)

@bp.route('/actions/')
def actions():
    actions = get_data('actions')

    #! this should go somewhere else
    types = ["Ability", "Spell"]

    return render_template('ffxiv/actions.html', actions=actions, types=types)

@bp.route('/items/', methods=('GET', 'POST'))
def items():
    items = get_data('items')

    if request.method == 'POST':
        name = request.form.get('name')
        Type = request.form.get('type')
        level = request.form.get('level')
        value = request.form.get('value')
        description = request.form.get('description')

        new_item = Item({'name':name, 'type':Type, 'description':description})
        items[new_item.name] = new_item

        set_data('items', items)

    return render_template('ffxiv/items.html', items=items, types=Item.TYPES)

@bp.route('/recipes/', methods=('GET', 'POST'))
def recipes():
    from .models import Recipe
    from .data import CRYSTALS

    if request.method == 'POST':
        return NotImplementedError
    
    recipes = get_data('recipes')
    items = get_data('items')

    return render_template('ffxiv/recipes.html', recipes=recipes, jobs=Job.JOBS, types=Recipe.TYPES, items=items, crystals=CRYSTALS)