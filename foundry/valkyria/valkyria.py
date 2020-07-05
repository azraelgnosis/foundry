from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from foundry.valkyria.db import ValkyriaDataManager
from foundry.valkyria.models import Potential, Soldier

bp = Blueprint('valkyria', __name__, url_prefix='/valkyria')
dm = ValkyriaDataManager()

@bp.route('/')
def index():
    return render_template('valkyria/index.html')

@bp.route('/soldiers/', methods=["GET"])
def soldiers():
    jobs = dm.get_jobs()
    soldiers = dm.get_soldiers()
    potentials = dm.get_potentials()

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

@bp.route('/potentials/', methods=['GET'])
def potentials() -> list:
    potentials = dm.get_potentials()

    return render_template('valkyria/potentials.html', potentials=potentials)

@bp.route('/potentials/', methods=['POST'])
def add_potential():
    new_potential = Potential.from_dict(request.form)

    potentials = dm.select('potentials', where={'potential_val': new_potential.val})

    error = None
    if potentials:
        error = "Potential already exists."

    if not error:
        dm.insert('potentials', new_potential.to_dict())

    flash(error)

    return redirect(url_for('valkyria.potentials'))