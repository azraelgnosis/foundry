from flask import (
    Blueprint, render_template
)

bp = Blueprint('ffxiv', __name__, subdomain='ffxiv')

@bp.route('/')
def index():
    return render_template('ffxiv/index.html')

@bp.route('/characters')
def characters(): ...

@bp.route('/characters/<character>')
def character(character): ...