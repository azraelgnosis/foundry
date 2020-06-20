import click
import os
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

from foundry.models import Row, User

class DataManager:
    def __init__(self, game:str=""):
        self.game = game

    def get_db(self) -> sqlite3.Connection:
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config["_".join(filter(None, ["DATABASE", self.game.upper()]))],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = Row

        return g.db

    def _where(self, conditions) -> str:
        """
        Creates an SQL WHERE clause based on `conditions`.
        If conditions is an instance of:
            str: returns conditions
            dict: returns AND-joined series where 'key = val'
            list:
                if 1-D:
                    if size 3: joins elements of list
                    if size 2: joins elements of list with =
                if 2-D: recursively calls _where()

        :param conditions: A string, dict, or list of conditions.
        :return: String of SQL WHERE clause.
        """

        WHERE = ""
        if isinstance(conditions, str):
            WHERE = conditions
        elif isinstance(conditions, dict):
            WHERE += \
                " AND ".join(
                    [f"{key} = '{val}'" for key, val in conditions.items()]
                )
        elif isinstance(conditions, list):
            if isinstance(conditions[0], list):
                WHERE += \
                    " AND ".join([self._where(condition) for condition in conditions])
            elif len(conditions) == 3:
                WHERE += " ".join(conditions)
            elif len(conditions) == 2:
                WHERE += " = ".join(conditions)

        return WHERE

    @staticmethod
    def _join(from_table:str, join:dict):
        """
        """

        joins = []
        for table, on in join.items():
            joins.append(f"LEFT JOIN {table} ON {table}.{on} = {from_table}.{on}")

        JOIN = "\t\n".join(joins)

        return JOIN

    def select(self, table:str, columns:list=['*'], join=None, where=None, datatype=None) -> list:
        """
        SELECT `columns` FROM `table`

        :param table:
        :param columns:
        """

        SELECT = "SELECT {columns}".format(columns=", ".join(columns))
        FROM = f"FROM {table}"
        JOIN = f"{self._join(table, join)}" if join else ""
        WHERE = f"WHERE {self._where(where)}" if where else ""

        results = self.get_db().execute("\n\t".join([SELECT, FROM, JOIN, WHERE])).fetchall()
        if datatype:
            results = [datatype.from_row(result) for result in results]

        return results

    def get_columns(self, table:str) -> list:
        """
        Retrieves a list of `table` columns.

        :param table: Name of database table.
        :return: List of columns.
        """

        cursor = self.get_db().execute(f"SELECT * FROM {table} LIMIT 0")
        columns = [col[0] for col in cursor.description]

        return columns

    def get_user(self, user_info): return User()
    def get_usernames(self): return []

    def insert(self, table:str, values:dict) -> None:
        """
        """

        INSERT = f"INSERT INTO `{table}`"
        cols = self.get_columns(table)[1:]
        COLUMNS = "({})".format(", ".join(cols))

        VALUES = "VALUES ({})".format(", ".join("?" * len(cols)))

        db = self.get_db()
        db.execute(
            " ".join([INSERT, COLUMNS, VALUES]),
            [f"{values.get(key)}" for key in cols]
        )
        db.commit()

    def update(self): ...


    def init_db(self, game):
        db = self.get_db()

        with current_app.open_resource(os.path.join(game, 'schema.sql')) as f:
            db.executescript(f.read().decode('utf8'))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
@click.argument('game', default='')
@with_appcontext
def init_db_command(game:str):
    """ Clear the existing data and create new tables."""
    DataManager(game).init_db(game)
    click.echo(f"Initialized the {game} database.")
