import sqlite3

from foundry.models import Model, Row

class Soldier(Model):
    __slots__ = ['soldier_id', 'name', 'soldier_val', 'sex', 'ethnicity_id', 'ethnicity_val', 'job_id', 'job_val', 'friends', 'potentials']
    fks = {'job': 'job_id'} #!

    # def init(self):
    #     self.name = self.soldier_val

class Job(Model):
    pass


class Potential(Model):
    __slots__ = ['potential_id', 'potential_val', 'potential_text']