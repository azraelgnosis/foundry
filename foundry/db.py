import click
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

from foundry.models import Row

class DataManager:
    def __init__(self, game:str):
        self.game = game

    def get_db(self) -> sqlite3.Connection:
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config[f"DATABASE_{self.game.upper()}"],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = Row

        return g.db

    def select(self, table:str, columns:list=['*'], coerce=False) -> list:
        """
        SELECT `columns` FROM `table`

        :param table:
        :param columns:
        """

        SELECT = "SELECT {columns}".format(columns=", ".join(columns))
        FROM = f"FROM {table}"
        WHERE = ""

        results = self.get_db().execute(" ".join([SELECT, FROM, WHERE])).fetchall()
        # if coerce and (datatype := types.get(table)):
        #     results = [datatype.from_row(result) for result in results]

        return results

    def init_db(self, game):
        db = self.get_db()

        with current_app.open_resource(f'{game}/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
@click.argument('game')
@with_appcontext
def init_db_command(game):
    """ Clear the existing data and create new tables."""
    DataManager(game).init_db(game)
    click.echo("Initialized the database.")