from flask import (
    Blueprint, render_template
)

bp = Blueprint("coc7", __name__, subdomain='coc7')

@bp.route('/')
def index():
    return render_template('coc7/index.html')

@bp.route('/characters/new', methods=('GET', 'POST'))
def new_character():
    return

@bp.route('/books/')
@bp.route('/books/<string:title>')
def books(title:str=""):
    if title:
        return render_template(f'coc7/books/{title}.html')
    return render_template('coc7/books/books.html')