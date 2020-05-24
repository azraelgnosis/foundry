import click
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

from foundry.dnd5.models import Row


def get_db() -> sqlite3.Connection:
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE_DND5'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = Row

    return g.db

def close_db(e=None) -> None:
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db() -> None:
    db = get_db()
    with current_app.open_resource('dnd5/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db-dnd5')
@with_appcontext
def init_db_command():
    """Clear the existing data nad create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
