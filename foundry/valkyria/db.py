import click
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3

from foundry.valkyria.models import Row, Soldier, Job, Potential

types = {
    "jobs": Job,
    "potentials": Potential,
    "soldiers": Soldier,
}

def get_db() -> sqlite3.Connection:
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE_VALKYRIA'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = Row

    return g.db

def select(table:str, columns:list=["*"], coerce=False) -> list:
    """
    SELECT `columns` FROM `table`

    :param table:
    :param columns:
    """

    SELECT = "SELECT {columns}".format(columns=", ".join(columns))
    FROM = f"FROM {table}"
    WHERE = ""
    
    results = get_db().execute(" ".join([SELECT, FROM, WHERE])).fetchall()
    if coerce and (datatype := types.get(table)):
        results = [datatype.from_row(result) for result in results]

    return results

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('valkyria/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-valkyria-db')
@with_appcontext
def init_db_command():
    """ Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)