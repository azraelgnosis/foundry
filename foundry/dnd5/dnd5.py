from flask import (
    Blueprint, render_template
)

from .data import get_spells

bp = Blueprint('dnd5', __name__, subdomain='dnd5')

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