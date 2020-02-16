from flask import (
    Blueprint, render_template
)

bp = Blueprint("coc7", __name__)

@bp.route('characters/new', methods=('GET', 'POST'))
def new_character():
    return