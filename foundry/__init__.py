import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE_FFXIV = os.path.join(app.instance_path, 'ffxiv', 'ffxiv.sqlite'),
        DATABASE_DEM3 = os.path.join(app.instance_path, 'dem3', 'dem3.sqlite'),
        DATABASE_DND5 = os.path.join(app.instance_path, 'dnd5', 'dnd5.sqlite'),
        DATABASE_VALKYRIA = os.path.join(app.instance_path, 'valkyria', 'valkyria.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import foundry
    app.register_blueprint(foundry.bp)

    from foundry.ffxiv import ffxiv, data
    app.register_blueprint(ffxiv.bp)
    data.init_app(app)

    from foundry.dnd5 import dnd5, db
    app.register_blueprint(dnd5.bp)
    db.init_app(app)

    from foundry.coc7 import coc7, data
    app.register_blueprint(coc7.bp)

    from foundry.valkyria import valkyria, db
    app.register_blueprint(valkyria.bp)
    db.init_app(app)

    return app