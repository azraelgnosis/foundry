from flask import (
    Blueprint, render_template
)

from foundry.db import DataManager

DM = DataManager()

bp = Blueprint("foundry", __name__)

@bp.route('/')
def index():
    return render_template("index.html")