import sqlite3

class Row(sqlite3.Row):
    def __init__(self, cursor, values):
        self.columns = [col[0] for col in cursor.description]
        self.val = values[1]

    def __repr__(self): return f"{self.val}"

class Model:
    __slots__ = ['id', 'val']

    def __init__(self):
        pass

    @classmethod
    def from_row(cls, row):
        new_obj = cls()

        return new_obj