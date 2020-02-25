from flask import (
    Blueprint, render_template
)

from .data import anyflip_books

bp = Blueprint("coc7", __name__, url_prefix='/coc7')

@bp.route('/')
def index():
    return render_template('coc7/index.html')

@bp.route('/characters/new', methods=('GET', 'POST'))
def new_character():
    return

@bp.route('/books/') #?
@bp.route('/books/<string:book>')
def books(book:str=""):
    if book:
        user = anyflip_books.get(book).get('user')
        code = anyflip_books.get(book).get('book')
        return render_template(f'coc7/book.html', user=user, code=code)
    return render_template('coc7/books/books.html')