from flask import (
    Blueprint, render_template
)

from foundry.valkyria.db import select

bp = Blueprint('valkyria', __name__, url_prefix='/valkyria')

@bp.route('/')
def index():
    return render_template('valkyria/index.html')

@bp.route('/soldiers/', methods=["GET"])
def soldiers():
    jobs = select("jobs")
    soldiers = select("soldiers")
    potentials = select("potentials")

    return render_template('valkyria/soldiers.html', jobs=jobs, soldiers=soldiers, potentials=potentials)