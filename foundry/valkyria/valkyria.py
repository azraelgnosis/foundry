from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from foundry.db import DataManager
from foundry.valkyria.models import Soldier


GAME = 'valkyria'
bp = Blueprint('valkyria', __name__, url_prefix='/valkyria')
dm = DataManager(GAME)

@bp.route('/')
def index():
    return render_template('valkyria/index.html')

@bp.route('/soldiers/', methods=["GET"])
def soldiers():
    jobs = dm.select("jobs")
    soldiers = dm.select("soldiers",
        columns=['soldier_val', 'ethnicity_val', 'job_val'],
        join={'ethnicities': ('ethnicity_id'), 'jobs': ('job_id')},
        datatype=Soldier)
    potentials = dm.select("potentials")

    return render_template('valkyria/soldiers.html', jobs=jobs, soldiers=soldiers, potentials=potentials)

@bp.route('/soldiers/', methods=['POST'])
def add_soldier():
    new_soldier = Soldier.from_dict(request.form)

    soldiers = dm.select('soldiers', where={'soldier_val': new_soldier.val})

    error = None
    if soldiers:
        error = "Soldier already exists."

    if not error:
        dm.insert('soldiers', new_soldier.to_dict())

    flash(error)

    return redirect(url_for('valkyria.soldiers'))
