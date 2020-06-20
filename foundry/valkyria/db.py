import click
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3

from foundry.db import DataManager
from foundry.valkyria.models import Row, Soldier, Job, Potential



types = {
    "jobs": Job,
    "potentials": Potential,
    "soldiers": Soldier,
}
