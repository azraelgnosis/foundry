from flask import (
    Blueprint, render_template, request
)

from .data import (
    WORLDS, search_character, get_character_api, get_data
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

@bp.route('/recipes/')
def recipes():
    from .models import Recipe
    from .data import CRYSTALS

    if request.method == 'POST':
        return NotImplementedError
    
    recipes = get_data('recipes')

    materials = []

    return render_template('ffxiv/recipes.html', recipes=recipes, jobs=Job.JOBS, types=Recipe.TYPES, materials=materials, crystals=CRYSTALS)