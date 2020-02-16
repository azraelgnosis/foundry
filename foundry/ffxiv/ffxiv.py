from flask import (
    Blueprint, render_template, request
)

from .data import WORLDS, search_character, get_character

bp = Blueprint('ffxiv', __name__, subdomain='ffxiv')

@bp.route('/', methods=('GET', 'POST'))
def index():
    characters = None

    if request.method == 'POST':
        name = request.form['name']
        server = request.form['server']

        characters = search_character(name, server)

    return render_template('ffxiv/index.html', worlds=WORLDS, characters=characters)

#????
@bp.route('/characters')
def characters(): ...

@bp.route('/characters/<int:id>')
def character(id):
    character = get_character(id)

    return render_template('ffxiv/character.html', character=character)
