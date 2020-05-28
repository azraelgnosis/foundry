import sqlite3

class Row(sqlite3.Row):
    pass

class Model:
    __slots__ = ['id', 'val']

    def __init__(self):
        pass

    @classmethod
    def from_row(cls, row):
        new_obj = cls()

        return new_obj

class Soldier(Model):
    __slots__ = ['job', 'friends', 'potentials']

class Job(Model):
    pass

class Potential(Model):
    pass