from flask import (
    Blueprint, render_template
)

from foundry.dnd5.data import get_spells, anyflip_books

bp = Blueprint('dnd5', __name__, url_prefix='/dnd5')

@bp.route('/')
def index():
    return render_template("dnd5/index.html")

@bp.route('/character/')
def character():
    return

@bp.route('/spells/')
def spells():
    spells = get_spells()
    return render_template("dnd5/spells.html", spells=spells)

@bp.route('/books/<string:book>')
def books(book):
    code = anyflip_books.get(book)
    return render_template(f'dnd5/book.html', book=code)