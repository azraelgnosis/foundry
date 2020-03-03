from flask import(
    Blueprint, render_template
)

bp = Blueprint('dem3', __name__, url_prefix='/dem3')

@bp.route('/')
def index():
    return render_template('dem3/index.html')