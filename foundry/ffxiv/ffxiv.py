from flask import (
    Blueprint, render_template, request
)
import json

from .data import (
    WORLDS, search_character, get_character_api, get_data, set_data
)
from .models import Character, Job

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
    actions = get_data("actions")

    #! this should go somewhere else
    types = ["Ability", "Spell"]

    return render_template('ffxiv/actions.html', actions=actions, types=types)

@bp.route('/materials/', methods=('GET', 'POST'))
def materials():
    from .models import Material
    from .data import VALUES

    materials = get_data('materials')

    if request.method == 'POST':
        name = request.form['name']
        Type = request.form['type']
        value = request.form['value']
        description = request.form['description']

        new_material = Material(name=name, type=Type, value=value, description=description)

        materials[new_material.name] = new_material.json()

        set_data('materials', materials)        

    return render_template('ffxiv/materials.html', materials=materials, jobs=Job.JOBS, types=Material.TYPES, values=VALUES)

@bp.route('/recipes/', methods=('GET', 'POST'))
def recipes():
    from .models import Recipe
    from .data import CRYSTALS

    if request.method == 'POST':
        return NotImplementedError
    
    recipes = get_data('recipes')

    materials = get_data('materials')

    return render_template('ffxiv/recipes.html', recipes=recipes, jobs=Job.JOBS, types=Recipe.TYPES, materials=materials, crystals=CRYSTALS)