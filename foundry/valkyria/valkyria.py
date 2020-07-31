from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from foundry.valkyria.models import Potential, Soldier
from foundry.valkyria.db import ValkyriaLoreKeeper

bp = Blueprint('valkyria', __name__, url_prefix='/valkyria')
lk = ValkyriaLoreKeeper()

@bp.route('/')
def index():
    return render_template('valkyria/index.html')

@bp.route('/soldiers/', methods=["GET"])
def soldiers():
    jobs = lk.get_jobs()
    soldiers = lk.get_soldiers()
    potentials = lk.get_potentials()

    return render_template('valkyria/soldiers.html', jobs=jobs, soldiers=soldiers, potentials=potentials)

@bp.route('/soldiers/', methods=['POST'])
def add_soldier():
    new_soldier = Soldier.from_dict(request.form)

    soldiers = lk.select('soldiers', where={'soldier_val': new_soldier.soldier_val})

    error = None
    if soldiers:
        error = "Soldier already exists."

    if not error:
        lk.insert('soldiers', new_soldier.to_dict())

    flash(error)

    return redirect(url_for('valkyria.soldiers'))

@bp.route('/potentials/', methods=['GET'])
def potentials() -> list:
    potentials = lk.get_potentials()

    return render_template('valkyria/potentials.html', potentials=potentials)

@bp.route('/potentials/', methods=['POST'])
def add_potential():
    new_potential = Potential.from_dict(request.form)

    potentials = lk.select('potentials', where={'potential_val': new_potential.val})

    error = None
    if potentials:
        error = "Potential already exists."

    if not error:
        lk.insert('potentials', new_potential.to_dict())

    flash(error)

    return redirect(url_for('valkyria.potentials'))