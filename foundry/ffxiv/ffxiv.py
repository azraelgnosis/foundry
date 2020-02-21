from flask import (
    Blueprint, render_template, request
)

from .data import WORLDS, search_character, get_character_api
from .models import Character

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
    return render_template('ffxiv/actions.html')