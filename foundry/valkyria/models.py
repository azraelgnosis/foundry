import sqlite3

from foundry.models import Model, Row

class Soldier(Model):
    __slots__ = ['job', 'friends', 'potentials']

class Job(Model):
    pass

class Potential(Model):
    pass