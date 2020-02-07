from flask import (
    Blueprint, render_template
)

bp = Blueprint('dnd5', __name__, subdomain='dnd5')

@bp.route('/')
def index():
    return 'hrm' # render_template("dnd5e/index.html")

