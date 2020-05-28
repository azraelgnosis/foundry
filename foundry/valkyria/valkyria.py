from flask import (
    Blueprint, render_template
)

bp = Blueprint('valkyria', __name__, url_prefix='/valkyria')

@bp.route('/')
def index():
    return render_template('valkyria/index.html')

@bp.route('/soldiers/')
def soldiers():
    return render_template('valkyria/soldiers.html')